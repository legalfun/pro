    start = datetime.now()
    url = 'https://coinmarketcap.com/all/views/all'
    all_links = get_all_links(get_html(url))
    for i, link in enumerate(all_links):
        html = get_html(link)
        data = get_page_data(html)
        write_csv(i, data)
    end = datetime.now()
    total = end - start
    print(str(total))
    a = input()

if __name__ == '__main__':
    main()