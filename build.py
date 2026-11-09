import json, pathlib, shutil
p=pathlib.Path(__file__).parent
items=json.loads((p/'content.json').read_text())
(p/'public'/'data.json').write_text(json.dumps(items,ensure_ascii=False))
for f in (p/'assets').glob('*'):shutil.copy2(f,p/'public'/f.name)
