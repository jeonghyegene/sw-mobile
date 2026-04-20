import re
import os

files = [
    "마이페이지-저장견적.html",
    "마이페이지-배송지관리.html",
    "마이페이지-고객관리.html",
    "마이페이지-파일보관함.html",
    "마이페이지-저장옵션.html",
    "마이페이지-현금영수증(발급내역).html",
    "마이페이지-현금영수증(신청).html",
    "마이페이지-세금계산서(발급내역).html",
    "마이페이지-세금계산서(신청).html",
    "마이페이지-세금계산서(신청서작성-단일).html",
    "마이페이지-세금계산서(신청서작성-다중).html",
    "마이페이지-성원머니.html",
    "마이페이지-성원머니(알럿모음).html",
    "마이페이지-성원머니(가상계좌환불계좌등록전).html",
    "마이페이지-성원포인트.html",
    "마이페이지-문의(목록).html",
    "마이페이지-문의(작성).html",
    "마이페이지-문의(상세-AS).html",
    "마이페이지-문의(상세-QNA).html",
    "마이페이지-문의(상세-답변없을때).html",
    "마이페이지-리뷰관리(작성가능한리뷰).html",
    "마이페이지-리뷰관리(작성한리뷰).html",
    "마이페이지-회원탈퇴.html",
    "마이페이지-회원탈퇴(SNS).html",
    "마이페이지-낮밤배송(신청전-메인).html"
]

for fname in files:
    if not os.path.exists(fname):
        continue
    
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all modals/sheets
    modals = set()
    modal_pattern = r'class="(modal-overlay|bottom-sheet-overlay)"[^>]*id="([^"]+)"'
    for match in re.finditer(modal_pattern, content):
        modals.add(match.group(2))
    
    # Find all RC buttons
    rc_buttons = set()
    rc_pattern = r"rc_open\('([^']+)'\)"
    for match in re.finditer(rc_pattern, content):
        rc_buttons.add(match.group(1))
    
    # Find missing
    missing = modals - rc_buttons
    
    print(f"\n[{fname}]")
    print(f"  모달/시트: {sorted(modals)}")
    print(f"  누락: {sorted(missing) if missing else '없음'}")
