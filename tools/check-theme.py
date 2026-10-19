#!/usr/bin/env python3
"""Read-only sanity check of a Playnite theme folder: XAML well-formedness, resource keys used by the
window-glass patch, options.yaml references (files, constants, localization keys), en/fr parity."""
import os, re, sys
import xml.etree.ElementTree as ET
import yaml

T = sys.argv[1]
X = '{http://schemas.microsoft.com/winfx/2006/xaml}Key'
errors, notes = [], []

keys, loc = {}, {}
for d, _, fs in os.walk(T):
    for f in fs:
        if not f.endswith('.xaml'):
            continue
        p = os.path.join(d, f)
        rel = os.path.relpath(p, T).replace(os.sep, '/')
        try:
            root = ET.fromstring(open(p, encoding='utf-8-sig').read().encode('utf-8'))
        except Exception as e:
            errors.append(f'XML {rel}: {e}')
            continue
        for el in root.iter():
            k = el.get(X)
            if k:
                keys.setdefault(k, set()).add(rel)
                if rel.startswith('Localization/'):
                    loc.setdefault(rel.split('/')[1][:-5], set()).add(k)

fullscreen = os.path.exists(os.path.join(T, 'theme.yaml')) and re.search(r'^Mode:\s*Fullscreen\s*$', open(os.path.join(T, 'theme.yaml'), encoding='utf-8-sig').read(), re.M) is not None
need = [] if fullscreen else ['WindowGlassEnabled', 'WindowGlassOpacity', 'WindowGlassBlurRadius', 'WindowGlassScrimOpacity', 'WindowGlassBleed', 'TopPanelGlassOpacity', 'SidebarGlassOpacity', 'LibraryPanelGlassOpacity', 'FilterPanelGlassOpacity']
for k in need:
    if k not in keys:
        errors.append(f'constant {k} not defined')

for lang in ('en_US', 'fr_FR'):
    if lang not in loc:
        errors.append(f'localization {lang} missing')
if set(loc.get('en_US', ())) != set(loc.get('fr_FR', ())):
    errors.append('en_US / fr_FR key sets differ: ' + str(sorted(set(loc['en_US']) ^ set(loc['fr_FR']))[:10]))

y = yaml.safe_load(open(os.path.join(T, 'options.yaml'), encoding='utf-8-sig').read())
n_const = n_loc = 0


def walk(n, path=''):
    global n_const, n_loc
    if isinstance(n, dict):
        for k, v in n.items():
            if k == 'LocKey' and isinstance(v, str):
                n_loc += 1
                if v not in loc.get('en_US', ()):
                    errors.append(f'options LocKey {v} ({path}) not in en_US')
            elif k == 'Preview' and isinstance(v, str):
                # under Variables, Preview names a preset (e.g. Buttons_Default), not an image path
                if v.lower().endswith('.png') and not os.path.exists(os.path.join(T, v.replace('\\', '/'))):
                    errors.append(f'options Preview missing: {v}')
            elif k == 'Files' and isinstance(v, list):
                for f in v:
                    if not os.path.exists(os.path.join(T, str(f).replace('\\', '/'))):
                        errors.append(f'options file missing: {f}')
            elif k == 'Constants' and isinstance(v, dict):
                for c in v:
                    n_const += 1
                    if c not in keys:
                        errors.append(f'options constant {c} ({path}) not defined in any xaml')
                walk(v, path + '/Constants')
            else:
                walk(v, path + '/' + str(k))
    elif isinstance(n, list):
        for i in n:
            walk(i, path)


walk(y)
for g in () if fullscreen else ('WindowDarkness', 'PanelGlass'):
    if g not in y['Presets']:
        errors.append(f'preset group {g} missing')
for v in () if fullscreen else ('WindowGlassEnabled', 'WindowGlassBlurRadius'):
    if v not in y['Variables']:
        errors.append(f'variable {v} missing')
notes.append(f'xaml keys: {len(keys)}; loc keys: {len(loc.get("en_US", ()))}; options constants checked: {n_const}; LocKeys checked: {n_loc}')

# every brush opacity patch present in every color preset
for f in [] if fullscreen else sorted(os.listdir(os.path.join(T, 'Presets', 'Colors'))):
    s = open(os.path.join(T, 'Presets', 'Colors', f), encoding='utf-8-sig').read()
    for b, z in (('TopPanelBackgroundBrush', 'TopPanelGlassOpacity'), ('SidebarBackgroundBrush', 'SidebarGlassOpacity'), ('LibraryDetailsViewBackgroundBrush', 'LibraryPanelGlassOpacity'), ('FilterPanelViewBackgroundBrush', 'FilterPanelGlassOpacity')):
        if not re.search(r'x:Key="%s"[^>]*%s' % (b, z), s):
            errors.append(f'Presets/Colors/{f}: {b} has no {z}')

print('\n'.join(notes))
print('ERRORS: %d' % len(errors))
for e in errors:
    print(' -', e)
sys.exit(1 if errors else 0)
