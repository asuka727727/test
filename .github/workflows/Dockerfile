# Pythonの公式イメージを使用
FROM python:3.12

# 作業ディレクトリを設定
WORKDIR /app

# 必要なライブラリをインストール
RUN apt-get update && apt-get install -y \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# OpenCVとその依存ライブラリをインストール
RUN pip install opencv-python

# アプリケーションのソースコードをコピー
COPY . .

# カメラデバイスをマッピング
# デフォルトのカメラデバイスが /dev/video0 以外の場合は適宜変更
--device /dev/video0:/dev/video0

# アプリケーションの実行
CMD ["streamlit", "run", "yoho_0.py"]
