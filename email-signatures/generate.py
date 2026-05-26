#!/usr/bin/env python3
"""Generate Mission Neptune email signatures (Forum + Permanente) for 4 team members.

Outputs 8 .htm files compatible with Outlook Windows (Word renderer), Outlook Mac,
Outlook Web, Apple Mail and Gmail. All images are referenced via the jsDelivr CDN
pointing to a versioned tag of the neptune-assets repo.

Usage:  python3 generate.py [CDN_TAG]
        (default tag: v1.2.0)
"""

import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).parent
CDN_BASE = "https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@{tag}/email-signatures/images"

PEOPLE = [
    {
        "slug": "adiceam",
        "name": "Ashok Adicéam",
        "role_fr": "Délégué Général",
        "role_en": "Executive Director",
        "phone_display": "+33 6 89 69 52 64",
        "phone_link": "+33689695264",
        "email": "ashok.adiceam@mission-neptune.com",
    },
    {
        "slug": "kisseleva",
        "name": "Daria Kisseleva",
        "role_fr": "Chargée de Mission",
        "role_en": "Communication Officer",
        "phone_display": "+33 6 98 30 83 34",
        "phone_link": "+33698308334",
        "email": "daria.kisseleva@mission-neptune.com",
    },
    {
        "slug": "lepivain",
        "name": "Anne-Sophie Le Pivain",
        "role_fr": "Chargée de Production",
        "role_en": "Production Officer",
        "phone_display": "+33 7 68 92 55 29",
        "phone_link": "+33768925529",
        "email": "intern@mission-neptune.com",
    },
    {
        "slug": "stojilkovic",
        "name": "Teodora Stojilkovic",
        "role_fr": "Chargée de Mission",
        "role_en": "Policy Officer",
        "phone_display": "+33 6 29 99 58 72",
        "phone_link": "+33629995872",
        "email": "teodora.stojilkovic@mission-neptune.com",
    },
    {
        "slug": "begards",
        "name": "Jade Bégards",
        "role_fr": "Chargée de Projet",
        "role_en": "Project Officer",
        "phone_display": "+33 7 87 36 59 52",
        "phone_link": "+33787365952",
        "email": "secretariat@mission-neptune.com",
    },
]

URL_FORUM = "https://mission-neptune.com/fr/the-forum"
URL_FILM = "https://mission-neptune.com/fr/the-mission"
URL_SITE = "https://mission-neptune.com"
SITE_DISPLAY = "www.mission-neptune.com"
ADDRESS = "195 Rue Saint-Jacques, 75005 Paris"

COLOR_NAVY = "#1D2B5C"
COLOR_TEXT = "#1A383A"
COLOR_MUTED = "#5A6B7A"

FONT = "Arial, Helvetica, sans-serif"


def forum_html(p: dict, cdn: str) -> str:
    return f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Signature {p["name"]} — Neptune Forum</title>
</head>
<body style="margin:0;padding:0;">
<table cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:collapse;font-family:{FONT};color:{COLOR_TEXT};">
  <tr>
    <td valign="top" width="185" style="width:185px;padding:0;">
      <a href="{URL_FORUM}" style="text-decoration:none;border:0;outline:none;">
        <img src="{cdn}/forum-panel-left.jpg" width="185" height="192" alt="Mission Neptune — Forum 6 au 8 Juin 2026" style="display:block;border:0;outline:none;text-decoration:none;width:185px;height:192px;" />
      </a>
    </td>
    <td valign="top" style="padding:6px 0 0 20px;font-family:{FONT};">
      <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:collapse;">
        <tr><td style="font-family:{FONT};font-size:17px;line-height:22px;color:{COLOR_TEXT};font-weight:bold;padding-bottom:2px;">{p["name"]}</td></tr>
        <tr><td style="font-family:{FONT};font-size:13px;line-height:18px;color:{COLOR_TEXT};padding-bottom:10px;">{p["role_fr"]} - <i>{p["role_en"]}</i></td></tr>
        <tr>
          <td style="font-family:{FONT};font-size:13px;line-height:20px;color:{COLOR_NAVY};padding-bottom:2px;">
            <img src="{cdn}/icon-phone.png" width="11" height="11" alt="" style="display:inline-block;border:0;vertical-align:middle;width:11px;height:11px;margin-right:8px;" />
            <a href="tel:{p["phone_link"]}" style="color:{COLOR_NAVY};text-decoration:none;">{p["phone_display"]}</a>
          </td>
        </tr>
        <tr>
          <td style="font-family:{FONT};font-size:13px;line-height:20px;color:{COLOR_NAVY};padding-bottom:12px;">
            <img src="{cdn}/icon-email.png" width="12" height="12" alt="" style="display:inline-block;border:0;vertical-align:middle;width:12px;height:12px;margin-right:7px;" />
            <a href="mailto:{p["email"]}" style="color:{COLOR_NAVY};text-decoration:none;">{p["email"]}</a>
          </td>
        </tr>
        <tr><td style="font-family:{FONT};font-size:13px;line-height:18px;color:{COLOR_TEXT};font-weight:bold;padding-bottom:1px;"><a href="{URL_FORUM}" style="color:{COLOR_TEXT};text-decoration:none;">NEPTUNE FORUM</a></td></tr>
        <tr><td style="font-family:{FONT};font-size:13px;line-height:18px;color:{COLOR_TEXT};">du 6 au 8 Juin 2026</td></tr>
        <tr><td style="font-family:{FONT};font-size:13px;line-height:18px;color:{COLOR_TEXT};padding-bottom:10px;">Muséum national d'Histoire naturelle - Paris</td></tr>
        <tr>
          <td style="font-family:{FONT};font-size:12px;line-height:18px;color:{COLOR_TEXT};">
            <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:collapse;">
              <tr>
                <td style="font-family:{FONT};font-size:12px;line-height:18px;color:{COLOR_TEXT};padding-right:18px;">
                  <a href="{URL_SITE}" style="color:{COLOR_TEXT};text-decoration:none;font-weight:bold;">{SITE_DISPLAY}</a> - {ADDRESS}
                </td>
                <td style="font-family:{FONT};font-size:12px;line-height:18px;color:{COLOR_TEXT};white-space:nowrap;">
                  <a href="{URL_FILM}" style="color:{COLOR_TEXT};text-decoration:none;font-weight:bold;letter-spacing:0.5px;">
                    VOIR LE FILM
                    <img src="{cdn}/play-icon.png" width="14" height="14" alt="" style="display:inline-block;border:0;vertical-align:middle;width:14px;height:14px;margin-left:6px;" />
                  </a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</body>
</html>
"""


def permanente_html(p: dict, cdn: str) -> str:
    return f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Signature {p["name"]} — Mission Neptune</title>
</head>
<body style="margin:0;padding:0;">
<table cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:collapse;font-family:{FONT};color:{COLOR_TEXT};">
  <tr>
    <td valign="top" style="padding:0 16px 0 0;font-family:{FONT};">
      <table cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:collapse;">
        <tr><td style="padding:0 0 8px 0;">
          <a href="{URL_SITE}" style="text-decoration:none;border:0;outline:none;">
            <img src="{cdn}/permanente-logo-left.png" width="140" height="34" alt="Mission Neptune" style="display:block;border:0;outline:none;text-decoration:none;width:140px;height:34px;" />
          </a>
        </td></tr>
        <tr><td style="font-family:{FONT};font-size:12px;line-height:16px;color:{COLOR_NAVY};font-weight:bold;padding-bottom:1px;">Explorer. Ressentir. Connaître. Protéger.</td></tr>
        <tr><td style="font-family:{FONT};font-size:11px;line-height:16px;color:{COLOR_TEXT};padding-bottom:14px;">
          <a href="{URL_SITE}" style="color:{COLOR_TEXT};text-decoration:none;">{SITE_DISPLAY}</a> - {ADDRESS}
        </td></tr>
        <tr><td style="font-family:{FONT};font-size:16px;line-height:20px;color:{COLOR_TEXT};font-weight:bold;padding-bottom:1px;">{p["name"]}</td></tr>
        <tr><td style="font-family:{FONT};font-size:12px;line-height:16px;color:{COLOR_TEXT};padding-bottom:8px;">{p["role_fr"]} - <i>{p["role_en"]}</i></td></tr>
        <tr>
          <td style="font-family:{FONT};font-size:12px;line-height:18px;color:{COLOR_NAVY};padding-bottom:2px;">
            <img src="{cdn}/icon-phone.png" width="11" height="11" alt="" style="display:inline-block;border:0;vertical-align:middle;width:11px;height:11px;margin-right:8px;" />
            <a href="tel:{p["phone_link"]}" style="color:{COLOR_NAVY};text-decoration:none;">{p["phone_display"]}</a>
          </td>
        </tr>
        <tr>
          <td style="font-family:{FONT};font-size:12px;line-height:18px;color:{COLOR_NAVY};">
            <img src="{cdn}/icon-email.png" width="12" height="12" alt="" style="display:inline-block;border:0;vertical-align:middle;width:12px;height:12px;margin-right:7px;" />
            <a href="mailto:{p["email"]}" style="color:{COLOR_NAVY};text-decoration:none;">{p["email"]}</a>
          </td>
        </tr>
      </table>
    </td>
    <td valign="top" width="320" style="width:320px;padding:0;">
      <a href="{URL_FILM}" style="text-decoration:none;border:0;outline:none;">
        <img src="{cdn}/permanente-reef-right.jpg" width="320" height="192" alt="Voir le film Mission Neptune" style="display:block;border:0;outline:none;text-decoration:none;width:320px;height:192px;" />
      </a>
    </td>
  </tr>
</table>
</body>
</html>
"""


def main():
    tag = sys.argv[1] if len(sys.argv) > 1 else "v1.2.0"
    cdn = CDN_BASE.format(tag=tag)
    forum_dir = ROOT / "forum"
    perm_dir = ROOT / "permanente"
    forum_dir.mkdir(exist_ok=True)
    perm_dir.mkdir(exist_ok=True)

    for p in PEOPLE:
        (forum_dir / f"{p['slug']}.htm").write_text(forum_html(p, cdn), encoding="utf-8")
        (perm_dir / f"{p['slug']}.htm").write_text(permanente_html(p, cdn), encoding="utf-8")
        print(f"  ✓ {p['slug']:14s} → forum + permanente")

    print(f"\nGenerated 8 signatures referencing CDN tag: {tag}")
    print(f"CDN base URL: {cdn}")


if __name__ == "__main__":
    main()
