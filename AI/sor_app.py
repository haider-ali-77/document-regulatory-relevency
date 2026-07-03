from fastapi import FastAPI
import json
import os
import re
import xml.etree.ElementTree as ET

app = FastAPI()

def get_heading_text(root):
    # For parsing headings in section level xml
    heading_text = ""
    text_lines = []
    for child in root:
        if child.tag in ["HEAD"]:
            text_line = ""
            for elm in child.itertext():
                text_line += elm
            text_lines.append(text_line)
    heading_text = "\n".join(text_lines)
    return heading_text

def get_full_text(root):
    # For parsing section level xml
    full_text = ""
    text_lines = []
    for child in root:
        if child.tag in ["P", "PSPACE", "FP", "P-1"]:
            text_line = ""
            for elm in child.itertext():
                text_line += elm
            text_lines.append(text_line)
    full_text = "\n".join(text_lines)
    return full_text

def text_matching_score(keyword, text):
    if keyword.lower() in text.lower():
        return 1
    return 0


keywords = ["cybersecurity", "information security", "data in transit","data storage","data retention","data archiving","data disposal", "sensitive data", "access management","device management","log management","penetration testing","encryption","Ransomware","Supply Chain Attack","Malicious emails","Darkweb","Virtual Private Network","VPN","IP Address","data Breach","Malware","Spyware","Phishing"]


def find_parent_items(hierarchy_items, overall_hierarchy):
    if not hierarchy_items:
        return hierarchy_items, overall_hierarchy
    min_div = min(int(x['DIV']) for x in hierarchy_items)
    # if 8 not in [int(x['DIV']) for x in hierarchy_items]:
    #     return [], overall_hierarchy
    parent_items = []
    if overall_hierarchy:
        parent_items = [y for y in overall_hierarchy[-1] if int(y['DIV'])<min_div]
    hierarchy_items = parent_items + hierarchy_items
    overall_hierarchy.append(hierarchy_items)
    hierarchy_items = []
    return hierarchy_items, overall_hierarchy

def filter_xml(root):
    thresh = 1
    for child in root.iter('DIV8'):
        section_matched = False
        for kw in keywords:
            full_text = get_full_text(child)
            heading_text = get_heading_text(child)
            if (text_matching_score(kw, heading_text) >= thresh) or (text_matching_score(kw, full_text) >= thresh):
                section_matched = True
                break
        if not section_matched:
            child.clear()

def create_hierarchy_items(root):
    hierarchy_items = []
    overall_hierarchy = []
    parent = root.find('DIV1')
    prev_hierarchy = 1
    curr_hierarchy = 1
    for child in parent.iter():
        hierarchy_json = {}
        tag_match = re.search(r"DIV(\d)", child.tag)
        if tag_match:
            prev_hierarchy = curr_hierarchy
            curr_hierarchy = int(tag_match.group(1))
            if curr_hierarchy <= prev_hierarchy:
                hierarchy_items, overall_hierarchy = find_parent_items(hierarchy_items, overall_hierarchy)
            hierarchy_json['DIV'] = tag_match.group(1)
            hierarchy_json['type'] = child.get('TYPE')
            # if child.find('HEAD') is None:
            #     hierarchy_items = []
            #     continue
            try:
                htmlstr = ET.tostring(child.find('HEAD'), encoding='unicode', method='html', xml_declaration=False)
            except Exception:
                htmlstr = ""
            hierarchy_json['heading'] = htmlstr
            hierarchy_json['body'] = ""
            if tag_match.group(1) == '8':
                try:
                    htmlstr = ET.tostring(child, encoding='unicode', method='html')
                except Exception:
                    htmlstr = ""
                htmlstr = re.sub(r'.*(?=<HEAD>)', "", htmlstr, count=1, flags=re.S)
                htmlstr = re.sub(r'</DIV8>.*', "", htmlstr, count=1, flags=re.S)
                hierarchy_json['body'] = htmlstr
            hierarchy_items.append(hierarchy_json)
    if hierarchy_items:
        hierarchy_items, overall_hierarchy = find_parent_items(hierarchy_items, overall_hierarchy)
    new_hierarchy = []
    for oh_ in overall_hierarchy:
        if not any(True for x in oh_ if (x['heading']=="")) and (8 in [int(x['DIV']) for x in oh_]):
            new_hierarchy.append(oh_)
    return new_hierarchy


def filter_xml_create_json(jurisdiction: str, project: str):
    os.makedirs(f"{project}/{jurisdiction}", exist_ok=True)
    base_path = os.getcwd()
    for file in os.listdir(jurisdiction):
        print (file)
        file_id = file.split('.')[0]
        full_path = os.path.join(base_path, jurisdiction, file)
        tree = ET.parse(full_path)
        root = tree.getroot()
        filter_xml(root)
        overall_hierarchy = create_hierarchy_items(root)
        tree.write(f"{project}/{jurisdiction}/{file_id}_filtered.xml")
        with open(f"{project}/{jurisdiction}/{file_id}.json",'w') as f:
            json.dump(overall_hierarchy, f)

@app.get("/view")
def fetch_hierarchy_json(jurisdiction: str, project: str):
    os.makedirs(f"{project}/{jurisdiction}", exist_ok=True)
    p_path = f"{project}/{jurisdiction}"
    base_path = os.getcwd()
    hierarchy_json = {}
    for file in os.listdir(p_path):
        if not file.endswith(".json"):
            continue
        file_id = file.split('.')[0]
        with open(f"{project}/{jurisdiction}/{file_id}.json",'r') as f:
            overall_hierarchy = json.load(f)
        hierarchy_json[file_id] = overall_hierarchy
    return hierarchy_json

# filter_xml_create_json("usa", "information_security")