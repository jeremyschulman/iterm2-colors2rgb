from lxml import etree

DEFAULT_FILENAME = "Untitled.itermcolors"

re_ns = {'re': 'http://exslt.org/regular-expressions'}


RGB_SEQUENCE = [
    'red',
    'green',
    'blue'
]


def iterm2_colors2rgb(filepath=None):
    et = etree.parse(filepath or DEFAULT_FILENAME)

    # extract the 16 "Ansi <n> Color" definitions
    color_keys = et.xpath('dict/key[starts-with(., "Ansi ")]')

    # there are 8 standard ANSI colors and 8 bright ANSI colors store these into
    # a dict as they are processed from the XML file; the key will be the color
    # index black=0, ... bright_white=15.  These values will not be stored in
    # sorted order, so will need to extract them in sorted order at the end of
    # this function.

    color_pallet = dict()

    # for each of the color definitions, extract the RGB color values

    for color_key in color_keys:
        color_id = int(color_key.text.split()[1])
        color_def = color_key.xpath('following-sibling::dict[1]')[0]
        rgb_def = extract_rgb(color_def)
        color_pallet[color_id] = rgb_def

    fg_rgb = extract_rgb(et.xpath('dict/key[. = "Foreground Color"]'
                                  '/following-sibling::dict[1]')[0])

    bg_rgb = extract_rgb(et.xpath('dict/key[. = "Background Color"]'
                                  '/following-sibling::dict[1]')[0])

    # return the colors in numerical sorted order (black=0, .. white=7, ...)

    color_pallet = [color_pallet[i] for i in sorted(color_pallet)]

    return bg_rgb, fg_rgb, color_pallet[0:9], color_pallet[9:]


def extract_rgb(color_def):
    rgb_def = [0, 0, 0]

    for color_code in color_def.xpath('key[re:match(., "Red|Green|Blue")]', namespaces=re_ns):
        rgb_seq = RGB_SEQUENCE.index(color_code.text.split()[0].lower())
        rgb_val = float(color_code.xpath("following-sibling::real[1]/text()")[0])
        rgb_val = round(rgb_val * 255)
        rgb_def[rgb_seq] = rgb_val

    return tuple(rgb_def)
