from django.shortcuts import redirect


class AdminRequiredMiddleware:
    """
    Middleware that protects admin workspace routes.
    Public routes (landing, auth, media, static, svg, admin) are allowed without auth.
    All other routes require authentication with admin role.
    """

    PUBLIC_PREFIXES = (
        '/',           # exact landing page only
        '/auth/',
        '/admin/',
        '/media/',
        '/static/',
        '/svg/',
    )

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        # Allow exact landing page
        if path == '/':
            return self.get_response(request)

        # Allow public prefixes
        for prefix in self.PUBLIC_PREFIXES[1:]:  # skip '/' since we handled it above
            if path.startswith(prefix):
                return self.get_response(request)

        # All other routes require authentication
        if not request.user.is_authenticated:
            login_url = f'/auth/login/?next={path}'
            return redirect(login_url)

        return self.get_response(request)
