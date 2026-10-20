for enc in ['utf-16', 'utf-8', 'latin-1']:
    try:
        with open(r"d:\cannaculture\index.html", "r", encoding=enc) as f:
            content = f.read()
            print(f"Leído exitosamente con {enc}, longitud {len(content)}")
            lines = [l for l in content.splitlines() if "bundle.js" in l or "script" in l.lower()]
            print(f"Líneas coincidentes ({len(lines)}):")
            for l in lines[-10:]:
                print("  ", l.strip())
            break
    except Exception as e:
        print(f"Fallo con {enc}: {e}")
