from django.shortcuts import redirect


def redirect_view(request):

    # ここにリダイレクト先の URL を入れる
    redirect_url = 'https://www.google.com'

    response = redirect(redirect_url, permanent=False)
    print(response)
    return response
