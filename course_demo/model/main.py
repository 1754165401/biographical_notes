from get_links import links_get
from get_page_links import get_page_links
from html_parse import parse
from save_html import save_html_sources


def main():
    list1 = links_get()
    list2 = get_page_links(list1)
    parse(save_html_sources(list2))
    print("运行完成")

main()