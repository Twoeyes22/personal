# Nginx 이미지를 기반으로 합니다
FROM nginx:latest

# 작업 디렉터리를 설정합니다 (관례에 따라 /app을 사용)
WORKDIR /app

# 현재 디렉터리의 모든 HTML 파일을 이미지의 Nginx 서비스 디렉터리로 복사합니다
COPY *.html /usr/share/nginx/html/

# 8080 포트를 노출합니다
EXPOSE 8080

# Nginx를 실행합니다 (daemon off 모드로 실행하여 컨테이너가 계속 실행되도록 합니다)
CMD ["nginx", "-g", "daemon off;"]
