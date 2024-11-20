# redirect-server-app

## このプロジェクトについて

指定された URL にリダイレクトするだけのアプリケーションです。

Django を使用しています。

## 実行方法

1. リポジトリをクローン
    ```
    git clone https://github.com/yuukis/redirect-server-app.git
    cd redirect-server-app
    ```

2. Django をインストール
    ```
    pip install django
    ```

3. redirectapp/views.py にリダイレクト先のURLを設定
   ```python
   def redirect_view(request):

     # ここにリダイレクト先の URL を入れる
     redirect_url = 'https://www.google.com'
   ``` 

4. アプリケーションを実行
   ```
   python manage.py runserver
   ```

5. http://localhost:8000/redirect/ にアクセス
