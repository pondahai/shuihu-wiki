# -*- coding: utf-8 -*-
"""全書設定:換一本書時,只需要改這個檔 + characters.py。

水滸傳(120回本)的回目是上下聯(「第一回 張天師祈禳瘟疫 洪太尉誤走妖魔」),
HEADING regex 有兩個標題群組;build_wiki 會自動串接所有非空群組。
正文前另有「引首」卷首文字,build_wiki 會輸出成獨立頁面。
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ── 書 ──────────────────────────────────────────────
BOOK_TITLE = "水滸傳"            # 用於 prompt 與網頁標題
N_CHAPTERS = 120                 # 全書回數(解析後檢查用)
RAW = ROOT / "data" / "shuihu_raw.txt"     # 原文純文字
EDITION_NOTE = "維基文庫 120 回本(zh-hant),全 120 回,含引首。"  # 首頁副標

# 章回標題:第(中文數字)回 上聯 下聯(fetch 已正規化為半形空格)
HEADING = re.compile(r"^第([一二三四五六七八九十百]+)回\s+(\S+)\s+(\S+)\s*$")

# 卷首文字(第一回之前)的頁面標題;無卷首的書設為 None
PREFACE_TITLE = "引首"

# ── 路徑 ────────────────────────────────────────────
VAULT = ROOT / "vault"
SITE = ROOT / "site"
FACTS = ROOT / "data" / "facts"

# ── LLM 端點(OpenAI 相容)──────────────────────────
API = "http://100.89.149.50:8002/v1/chat/completions"
MODEL = "nvidia/Qwen3.6-35B-A3B-NVFP4"
