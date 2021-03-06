import re

def current_id_replacements(current_id):
    current_id = current_id.replace('<h1 class="title" id="firstHeading">', '')
    current_id = current_id.replace('</h1>', '')
    return current_id


def verse_replacements(verse):
    verse = verse.replace('<div class="verse">', '')
    verse = verse.replace('</div>', '')
    verse = verse.replace('<dl>', '---')
    verse = verse.replace('</dl>', '')
    verse = verse.replace('<dd>', '')
    verse = verse.replace('</dd>', '')
    return verse


def synonyms_replacements(synonyms):
    synonyms = synonyms.replace('<div class="synonyms">', '')
    synonyms = synonyms.replace('<p>', '')
    synonyms = synonyms.replace('<i>', '')
    synonyms = synonyms.replace('</i>', '')
    synonyms = synonyms.replace('</p>', '')
    synonyms = synonyms.replace('</div>', '')
    return synonyms


def translation_replacements(translation):
    translation = translation.replace('<div class="translation">', '')
    translation = translation.replace('<p>', '')
    translation = translation.replace('</p>', '')
    translation = translation.replace('</div>', '')
    return translation

def purport_replacements(purport):
    purport = purport.replace('</p>', '---')
    purport = purport.replace('[<div class="purport">', '')
    purport = purport.replace('<p>', '')
    purport = purport.replace('<i>', '')
    purport = purport.replace('</i>', '')
    purport = purport.replace('</div>]', '')
    purport = purport.replace('</dl>', '---')
    purport = purport.replace('<dl>', 'verse>>>')
    purport = purport.replace('<dd>', '')
    purport = purport.replace('</dd>', '')
    purport = re.sub('(\(<a.*?/a>\))','',purport)
    purport = re.sub('(<a.*?/a>)','',purport)
    purport = purport.replace('<b>', '')
    purport = purport.replace('</b>', '')

    return purport