import bcrypt

# 회원가입 할 때, 비번 해시를 생성하는 함수
def hash_password(plain_password: str):
    password_hash_bytes: bytes = bcrypt.hashpw(
        plain_password.encode(), bcrypt.gensalt(),
    )
    return password_hash_bytes.decode()

# 로그인 할 때, 비밀번호를 검증하는 함수
def verify_password(plain_password: str, password_hash: str) -> bool:
    try:
        # 1. 괄호와 오타 수정: encode()로 변경
        # 2. bcrypt.checkpw의 인자 괄호 정확히 닫기
        return bcrypt.checkpw(
            plain_password.encode(), 
            password_hash.encode()
        )
    except Exception:
        return False