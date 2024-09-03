# SemiProject v1b

## 프로젝트에 사용한 모듈들
+ FastAPI, uvicorn
+ Jinja2
+ sqlalchemy

## 프로젝트 기본 구조
+ 설정 (디비 서버): dbfactory, settings
+ model (디비-테이블) : Member
+ schema (유효성 검사) : NewMember
+ service (CRUD - 기능구현): MemberService
+ route (url - 엔드포인트 제공): member_router

## nginx 설정 추가
```
location / {
	# root   /usr/share/nginx/html;
	# index  index.html index.htm;

    # 프록시 설정
	proxy_pass http://localhost:8000;
	proxy_set_header Host $host;
	proxy_set_header X-Real-IP $remote_addr;
	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	proxy_set_header X-Forwarded-Proto $scheme;

	# gzip 압축을 활성화합니다.
	gzip on;
	gzip_types text/plain application/xml application/json text/css text/javascript application/javascript;
	gzip_min_length 1000;
}
```

```
# 정적 파일 서빙
location /static/ {
    alias /usr/share/nginx/html/static/;
    #expires 30d;
    #add_header Cache-Control "public, max-age=2592000";
}

location /cdn/img/ {
    alias /usr/share/nginx/html/cdn/img/;
}
```