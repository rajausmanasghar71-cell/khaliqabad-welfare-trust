import yaml, html, os
data=yaml.safe_load(open("content/site.yml",encoding="utf-8"))
template=open("index.template.html",encoding="utf-8").read()
cards="".join(f'<article class="card"><h3>{html.escape(x.get("title",""))}</h3><p>{html.escape(x.get("description",""))}</p></article>' for x in data.get("works",[]))
gallery=""
for x in data.get("gallery",[]):
    img=x.get("image","")
    if img:
        gallery += f'<figure><img src="{html.escape(img)}" alt="{html.escape(x.get("caption",""))}"><figcaption>{html.escape(x.get("caption",""))}</figcaption></figure>'
wa=data.get("whatsapp","").strip()
wab=f'<a class="btn" href="{html.escape(wa)}" target="_blank">WhatsApp</a>' if wa else ""
out=template.replace("{{TITLE}}",html.escape(data.get("title",""))).replace("{{INTRO}}",html.escape(data.get("intro",""))).replace("{{ABOUT}}",html.escape(data.get("about",""))).replace("{{CONTACT}}",html.escape(data.get("contact",""))).replace("{{FACEBOOK}}",html.escape(data.get("facebook",""))).replace("{{WORK_CARDS}}",cards).replace("{{GALLERY}}",gallery).replace("{{WHATSAPP_BUTTON}}",wab)
open("index.html","w",encoding="utf-8").write(out)
