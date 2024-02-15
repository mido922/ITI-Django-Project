from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from .models import Profile


# Register User
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            isEmailFound = User.objects.filter(email=request.POST["email"]).exists()
            if not isEmailFound:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                profile = Profile.objects.get(user=user)

                # Generate activation token
                token_generator = default_token_generator
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = token_generator.make_token(user)

                # Set expiration time for the activation link (24 hours from now)
                expiration_time = timezone.now() + timedelta(hours=24)
                profile.activation_token = token
                profile.activation_token_expires_at = expiration_time
                profile.save()

                # Construct activation link
                activation_link = f"http://127.0.0.1:9000/user/activate/{uid}/{token}"
                # Send activation email
                subject = "Activate your account"
                message = render_to_string(
                    "registration/activation_email.html",
                    {"activation_link": activation_link},
                )
                send_mail(subject, message, "from@example.com", [user.email])
                messages.info(
                    request, "Please check your email to activate your account."
                )
            else:
                messages.warning(request, "This account is Already Found")
                
        return redirect("home")
    else:
        form = UserRegisterForm()
        return render(request, "registration/signup.html", {"form": form})


# Activation Email
def activate(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        user_profile = Profile.objects.get(user=user)
    except (
        TypeError,
        ValueError,
        OverflowError,
        User.DoesNotExist,
        Profile.DoesNotExist,
    ):
        user = None
        user_profile = None

    token_generator = default_token_generator
    if (
        user is not None
        and user_profile is not None
        and token_generator.check_token(user, token)
    ):
        if not user.is_active and user_profile.is_activation_link_valid():
            # Activate the user account
            user.is_active = True
            user.save()
            messages.success(request, "Your account has been activated successfully.")
            return redirect("home")
        else:
            if not user.is_active:
                messages.warning(request, "Your account is already activated")
            elif user_profile.is_activation_link_valid():
                messages.error(request, "The activation link has expired.")
            return redirect("home")
    else:
        return HttpResponse("Activation link is invalid.")


# def reSendActivationMail():
#     pass

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "registration/profile.html", context)
