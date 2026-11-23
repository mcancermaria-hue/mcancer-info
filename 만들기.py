# AI 안내 페이지 생성기 — 사실·질문·답은 여기 한 곳에서 고치고 `python3 만들기.py` 로 다시 만든다.
# 모든 사실은 www.mcancer.com 실제 화면(2026-11-23)과 brand-master.md 에서 옮겼다. 지어낸 값 없음.
import json, html, datetime
BASE = "https://mcancermaria-hue.github.io/mcancer-info/"   # 주소가 정해지면 여기만 바꾼다
MAIN = "https://www.mcancer.com"
TODAY = datetime.date.today().isoformat()

ORG = {
 "name":"마뗄암재단","legal":"재단법인 마뗄암재단","en":"Mater Cancer Foundation",
 "intro":"마뗄암재단은 종교와 형편에 상관없이 암환자와 가족의 몸과 마음을 돌보는 비영리 재단입니다. 쉬고, 마음을 나누고, 치료를 이어 갈 수 있도록 함께합니다.",
 "history":"2004년 12월 한국순교복자수녀회가 세웠고, 2005년 8월 보건복지부에서 비영리법인 인가를 받았습니다. 일반 기부금단체입니다.",
 "id":"121-82-11061",
}

PROGRAMS = [
 {"name":"희망의 꽃","url":"/retreat","free":True,
  "one":"치료 중인 암환자가 강화 마뗄 쉼터에서 3박 4일 동안 머물며 쉼과 위로를 얻는 무료 정서지원 프로그램입니다.",
  "rows":[("대상","치료 중인 암환자 본인 · 종교와 관계없이"),("기간","3박 4일 · 월요일 오후 3시에 들어와 목요일 오후 1시에 나갑니다"),
          ("정원","회당 10명 이내 · 한 해 18회"),("비용","무료 (숙박·식사·프로그램 모두)"),("장소","강화 마뗄 쉼터 (인천 강화군 화도면)"),
          ("교통","김포 구래역까지 오시면 재단 차량으로 마중과 배웅을 합니다"),("신청","전화 010-3355-1946")]},
 {"name":"사랑이 핀 쉼터","url":"/stay","free":True,
  "one":"치료 중인 암환자와 가족(보호자)이 강화 마뗄 쉼터에서 한 번에 최대 4박 5일 무료로 머무는 쉼터입니다.",
  "rows":[("대상","치료 중인 암환자와 가족(보호자) · 성별 제한 없음 · 종교와 관계없이"),("기간","한 번에 최대 4박 5일 · 요일은 자유, 날짜는 전화로 정합니다"),
          ("비용","무료"),("식사","점심은 쉼터에서 드립니다. 나머지 식사는 주방에서 직접 준비합니다"),("방","개인실 · 가족실, 침구 제공"),
          ("지켜 주실 것","담배·술·반려동물 동반 불가"),("신청","강화 마뗄 쉼터 전화 032-937-7530")]},
 {"name":"진료비 지원","url":"/treatment","free":False,
  "one":"치료비 마련이 어려운 복지 사각지대의 암환자에게 치료에 직접 드는 진료비의 일부를 지원합니다.",
  "rows":[("대상","암 진단을 받고 치료 중이며 진료비 마련이 어려운 분 · 복지 사각지대 암환자 우선"),("지원 항목","진단비 · 수술비 · 항암치료비 · 방사선치료비 (진료비의 일부)"),
          ("신청","치료받는 병원의 사회사업팀(사회사업과)을 통해서만 신청합니다. 암환자가 재단에 직접 내지 않습니다"),("결정","재단 지원심사위원회가 심의해 정합니다")]},
 {"name":"가브리엘라 천사의 집","url":"/gabriel","free":True,
  "one":"더 이상 치료가 어려운 말기 암환자와 가족이 남겨진 시간을 함께 보내도록 강화도에 지은 무료 쉼터입니다. 2027년 1월 개원 예정입니다.",
  "rows":[("대상","더 이상 치료가 어려운 말기 암환자와 가족"),("비용","무료"),("위치","인천광역시 강화군 화도면 안골길61번길 17-12 · 지상 3층"),
          ("개원","2027년 1월 예정"),("문의","전화 032-937-7311")]},
]

PLACES = [
 ("재단 본부 · 사무국 (서울)","서울특별시 종로구 자하문로19길 7 (03035)","휴대전화 010-3355-1946 · 전화 02-723-4706 · 팩스 02-722-1940 · 이메일 mcancer1946@gmail.com"),
 ("강화 마뗄 쉼터 (희망의 꽃 · 사랑이 핀 쉼터)","인천광역시 강화군 화도면 마니산로731번길 15","전화 032-937-7530 · 팩스 032-937-7531 · 화도터미널(화도초등학교 앞) 정류장에서 걸어서 5분"),
 ("가브리엘라 천사의 집 (2027년 1월 개원 예정)","인천광역시 강화군 화도면 안골길61번길 17-12","전화 032-937-7311 · 팩스 032-937-7511"),
]

# 질문은 따로 떼어 읽어도 뜻이 통하게 사업 이름을 넣었다. 답은 www.mcancer.com/faq 글 그대로.
FAQ = [
 ("마뗄암재단 지원은 어떻게 신청하나요?","지원마다 신청하는 곳이 다릅니다. 희망의 꽃은 재단 010-3355-1946으로, 사랑이 핀 쉼터는 강화 마뗄 쉼터 032-937-7530으로 전화해 주세요. 진료비 지원은 치료받는 병원의 사회사업팀에 말씀해 주세요. 사회사업팀이 재단에 신청서를 냅니다."),
 ("희망의 꽃이나 사랑이 핀 쉼터도 신청서를 써야 하나요?","희망의 꽃과 사랑이 핀 쉼터는 신청서가 없습니다. 전화만 하시면 됩니다. 진료비 지원만 \"암환자 진료비 지원신청서(재단 양식)\"를 씁니다. 병원 사회사업팀이 함께 작성해 재단에 냅니다."),
 ("종교가 없어도 마뗄암재단 지원을 받을 수 있나요?","네, 종교와 관계없이 참여할 수 있습니다."),
 ("사랑이 핀 쉼터는 누가 이용할 수 있나요?","치료 중인 암환자와 가족(보호자)이면 종교와 관계없이 이용하실 수 있습니다. 개인실과 가족실이 있습니다."),
 ("사랑이 핀 쉼터 이용료가 있나요?","없습니다. 종교와 형편에 상관없이, 누구나 무료로 머무실 수 있습니다."),
 ("사랑이 핀 쉼터에는 며칠 머물 수 있나요?","한 번에 최대 4박 5일 머무실 수 있습니다. 요일은 정해져 있지 않습니다. 원하시는 날짜를 전화로 정해 주세요. 들어오시는 시간과 나가시는 시간은 전화로 안내해 드립니다."),
 ("사랑이 핀 쉼터에서 식사는 어떻게 하나요?","점심은 쉼터에서 드립니다. 아침과 저녁은 직접 준비해 주세요. 주방을 쓰실 수 있습니다."),
 ("희망의 꽃은 어떻게 진행하나요?","강화 마뗄 쉼터에서 3박 4일을 함께 지냅니다. 월요일 오후 3시에 들어와 목요일 오후 1시에 나갑니다. 한 번에 10명 이내가 참가합니다. 세 끼 식사를 모두 드립니다. 첫날은 서로 이야기를 나누고, 둘째 날은 강의와 개별 상담이 있습니다. 셋째 날은 갯벌에 나가고, 마지막 날 소감을 나눈 뒤 돌아갑니다."),
 ("희망의 꽃에는 누가 참가할 수 있나요?","암 진단을 받고 치료 중인 암환자가 참가합니다. 암환자 중심으로 진행하며, 종교와 관계없이 신청하실 수 있습니다. 전화하시면 일정을 함께 정합니다."),
 ("희망의 꽃 참가비가 있나요?","없습니다. 숙박 · 식사 · 프로그램 모두 무료입니다."),
 ("희망의 꽃에 가족과 함께 갈 수 있나요?","희망의 꽃은 암환자 한 분이 온전히 자신을 돌보는 시간이라 암환자 중심으로 진행합니다. 가족과 함께 쉬고 싶으시면 사랑이 핀 쉼터를 이용해 주세요."),
 ("희망의 꽃은 강화까지 어떻게 가나요?","김포 구래역까지 오시면 재단 차량으로 마중을 갑니다. 돌아가실 때도 구래역까지 배웅을 합니다."),
 ("암환자 진료비 지원은 어떻게 신청하나요?","치료받는 병원의 사회사업팀(사회사업과)에서만 신청할 수 있습니다. 암환자가 재단에 직접 내는 방식이 아닙니다. 사회사업팀이 신청서를 내면 재단 지원심사위원회가 심의해 결정합니다."),
 ("마뗄암재단 진료비 지원은 누가 받을 수 있나요?","치료비 마련이 어려운 암환자를 지원합니다. 복지 사각지대에 계신 분을 먼저 살핍니다. 따로 정해 둔 소득 기준선은 없습니다. 병원 사회사업팀이 신청하면 재단이 심의해 정합니다. 다른 제도의 지원을 받고 있어도 신청하실 수 있습니다. 재단은 다른 제도로 감당되지 않는 자기부담분을 지원합니다."),
 ("진료비 지원에는 어떤 서류가 필요하나요?","진료비 지원신청서 · 환자생활실태조사서(재단 양식) · 진단서 · 주치의 치료계획서 · 주민등록등본 · 건강보험증 또는 의료급여증 사본 · 수급자증명서(수급자인 경우만). 서류는 병원 사회사업팀이 안내해 드립니다."),
 ("진료비 지원은 얼마까지 받을 수 있나요?","재단은 치료에 직접 드는 진료비의 일부를 지원합니다. 지원 범위는 심의 뒤에 정합니다."),
 ("마뗄암재단 기부금 영수증은 어떻게 받나요?","마뗄암재단은 보건복지부 인가 비영리법인이자 일반 기부금단체로, 연말정산 때 세액공제를 받으실 수 있습니다. 기부금 영수증은 사무국(010-3355-1946 · 02-723-4706)에 요청하시면 발급해 드립니다."),
 ("마뗄암재단 정기 후원을 멈추거나 금액을 바꾸려면 어떻게 하나요?","재단 010-3355-1946 · 02-723-4706으로 전화 주시거나 mcancer1946@gmail.com으로 알려 주시면 바로 처리해 드립니다. 후원 금액을 바꾸실 때도 같은 방법으로 알려 주세요."),
]

GIVE = [("우리은행","1005-400-984764"),("농협은행","355-0064-3508-93")]

e = html.escape
def ld():
    org = {"@context":"https://schema.org","@type":"NGO","@id":MAIN.replace("www.","")+"/#org","name":ORG["name"],"legalName":ORG["legal"],
      "alternateName":[ORG["en"]],"url":"https://mcancer.com/","foundingDate":"2004","description":ORG["intro"],
      "identifier":{"@type":"PropertyValue","propertyID":"고유번호","value":ORG["id"]},
      "email":"mcancer1946@gmail.com","telephone":"+82-2-723-4706","faxNumber":"+82-2-722-1940",
      "address":{"@type":"PostalAddress","streetAddress":"자하문로19길 7","addressLocality":"종로구","addressRegion":"서울특별시","postalCode":"03035","addressCountry":"KR"},
      "sameAs":["https://www.youtube.com/@matercancer", BASE],
      "makesOffer":[{"@type":"Offer",**({"price":"0","priceCurrency":"KRW"} if p["free"] else {}),
         "itemOffered":{"@type":"Service","name":p["name"],"description":p["one"],"url":MAIN+p["url"]}} for p in PROGRAMS]}
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}
    page = {"@context":"https://schema.org","@type":"WebPage","name":"마뗄암재단 한눈에 보기","url":BASE,"inLanguage":"ko","dateModified":TODAY,"about":{"@id":org["@id"]}}
    return "\n".join('<script type="application/ld+json">'+json.dumps(x,ensure_ascii=False,separators=(",",":"))+'</script>' for x in (org,page,faq))

def table(rows): return "<dl>"+"".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k,v in rows)+"</dl>"

body = f"""
<header class="top"><div class="wrap"><p class="eye">재단법인 마뗄암재단 · {e(ORG['en'])}</p>
<h1>마뗄암재단 한눈에 보기</h1>
<p class="lead">{e(ORG['intro'])}</p>
<p class="note">이 페이지는 마뗄암재단 공식 홈페이지 <a href="{MAIN}/">www.mcancer.com</a>의 내용을 한 장에 모은 안내입니다. 자세한 내용과 사진은 공식 홈페이지에서 보실 수 있습니다.</p></div></header>
<main class="wrap">
<section id="about"><h2>마뗄암재단은 어떤 곳인가요?</h2>
<p>{e(ORG['intro'])} {e(ORG['history'])}</p>
<p>하는 일은 네 가지입니다. 암환자의 마음을 돌보는 <b>희망의 꽃</b>, 암환자와 가족이 함께 쉬는 <b>사랑이 핀 쉼터</b>, 치료를 이어 가게 돕는 <b>진료비 지원</b>, 말기 암환자와 가족을 위한 <b>가브리엘라 천사의 집</b>입니다. 희망의 꽃·사랑이 핀 쉼터·가브리엘라 천사의 집은 무료입니다.</p>
<p class="meta">고유번호 {ORG['id']} · 이사장 이순이 수녀 · <a href="{MAIN}/about">재단 소개 보기</a></p></section>
"""
for p in PROGRAMS:
    body += f"""<section id="{e(p['url'].strip('/'))}"><h2>{e(p['name'])}{' <span class="free">무료</span>' if p['free'] else ''}</h2>
<p class="one">{e(p['one'])}</p>{table(p['rows'])}<p class="more"><a href="{MAIN}{p['url']}">{e(p['name'])} 자세히 보기 ›</a></p></section>
"""
body += '<section id="contact"><h2>연락처와 주소</h2>' + "".join(f"<div class='place'><h3>{e(n)}</h3><p>{e(a)}</p><p class='meta'>{e(t)}</p></div>" for n,a,t in PLACES) + f'<p class="more"><a href="{MAIN}/map">오시는 길 보기 ›</a></p></section>\n'
body += '<section id="give"><h2>후원은 어떻게 하나요?</h2><p>보내 주신 후원은 진료비 지원, 희망의 꽃과 쉼터, 가브리엘라 천사의 집 운영에 쓰입니다. 정기 후원(자동이체)은 공식 홈페이지에서 신청하실 수 있고, 전화로도 안내해 드립니다.</p>' + table([(b,n) for b,n in GIVE]+[("예금주","재단법인 마뗄암재단")]) + f'<p>마뗄암재단은 보건복지부 인가 비영리법인이자 일반 기부금단체로, 연말정산 때 세액공제를 받으실 수 있습니다.</p><p class="more"><a href="{MAIN}/guide">후원 안내 보기 ›</a></p></section>\n'
body += '<section id="faq"><h2>자주 묻는 질문</h2>' + "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q,a in FAQ) + f'<p class="more"><a href="{MAIN}/faq">자주 묻는 질문 전체 보기 ›</a></p></section>\n</main>\n'
body += f'<footer><div class="wrap"><p>재단법인 마뗄암재단 | 고유번호 {ORG["id"]} | 서울특별시 종로구 자하문로19길 7 (03035) | 전화 010-3355-1946 · 02-723-4706 | 이메일 mcancer1946@gmail.com</p><p>공식 홈페이지 <a href="{MAIN}/">www.mcancer.com</a> · 마지막 확인 {TODAY}</p></div></footer>'

css = """:root{--teal:#006D6B;--ink:#22312F;--mint:#DDF2F0;--line:#DDE5E4;--mute:#5f6b69}
*{box-sizing:border-box}body{margin:0;background:#fff;color:var(--ink);font-family:Pretendard,"Pretendard Variable",-apple-system,"Apple SD Gothic Neo","Noto Sans KR",sans-serif;font-size:18px;line-height:1.8;word-break:keep-all}
a{color:var(--teal)}.wrap{max-width:860px;margin:0 auto;padding:0 20px}
.top{background:var(--mint);padding:48px 0 36px}.eye{margin:0;color:var(--teal);font-weight:700;font-size:16px}
h1{font-size:40px;line-height:1.3;margin:6px 0 14px}.lead{font-size:20px;margin:0 0 12px}.note{font-size:16px;color:var(--mute);margin:0}
section{padding:40px 0;border-bottom:1px solid var(--line)}h2{font-size:28px;line-height:1.35;margin:0 0 14px}h3{font-size:20px;margin:0 0 4px}
.free{display:inline-block;vertical-align:middle;font-size:15px;background:#FFCF3F;color:#3a2f05;border-radius:999px;padding:2px 12px;margin-left:6px}
.one{font-size:20px;font-weight:600}dl{display:grid;grid-template-columns:8.5em 1fr;gap:8px 16px;margin:16px 0}dt{font-weight:700;color:var(--teal)}dd{margin:0}
.meta{font-size:16px;color:var(--mute)}.more{margin:12px 0 0;font-weight:700}.place{margin:0 0 20px}.place p{margin:0}
details{border:1px solid var(--line);border-radius:12px;padding:12px 18px;margin:0 0 10px}summary{font-weight:700;cursor:pointer}details p{margin:10px 0 0}
footer{background:#f6f8f8;padding:28px 0;font-size:15px;color:var(--mute)}footer p{margin:4px 0}
@media(max-width:600px){h1{font-size:32px}h2{font-size:24px}dl{grid-template-columns:1fr;gap:2px}dt{margin-top:8px}}"""

page = f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>마뗄암재단 한눈에 보기 | 암환자·가족 무료 쉼터와 진료비 지원</title>
<meta name="description" content="마뗄암재단은 종교와 형편에 상관없이 암환자와 가족을 돕는 비영리 재단입니다. 희망의 꽃(암환자 3박 4일 무료), 사랑이 핀 쉼터(최대 4박 5일 무료), 진료비 지원, 가브리엘라 천사의 집 안내와 연락처.">
<link rel="canonical" href="{BASE}"><meta property="og:title" content="마뗄암재단 한눈에 보기"><meta property="og:url" content="{BASE}"><meta property="og:type" content="website">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>{css}</style>
{ld()}
</head><body>{body}</body></html>
"""
open("index.html","w").write(page)

llms = f"""# 마뗄암재단 (재단법인 마뗄암재단, Mater Cancer Foundation)

> {ORG['intro']} {ORG['history']} 공식 홈페이지는 {MAIN}/ 입니다.

## 하는 일
""" + "".join(f"- [{p['name']}]({MAIN}{p['url']}): {p['one']}\n" for p in PROGRAMS) + f"""
## 연락처
""" + "".join(f"- {n}: {a} / {t}\n" for n,a,t in PLACES) + f"""
## 후원
- 후원 계좌: 우리은행 1005-400-984764, 농협은행 355-0064-3508-93 (예금주 재단법인 마뗄암재단)
- 보건복지부 인가 비영리법인이자 일반 기부금단체. 기부금 영수증은 사무국 010-3355-1946 · 02-723-4706
- [후원 안내]({MAIN}/guide)

## 자주 묻는 질문
""" + "".join(f"- {q} {a}\n" for q,a in FAQ) + f"""
## 페이지
- [한눈에 보기]({BASE}): 이 내용을 한 장에 모은 안내
- [자주 묻는 질문 전체]({MAIN}/faq)
- [오시는 길]({MAIN}/map)

마지막 확인: {TODAY}
"""
open("llms.txt","w").write(llms)
open("robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
open("sitemap.xml","w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{BASE}</loc><lastmod>{TODAY}</lastmod></url><url><loc>{BASE}llms.txt</loc><lastmod>{TODAY}</lastmod></url></urlset>\n')
print("ok", len(page), len(llms))
