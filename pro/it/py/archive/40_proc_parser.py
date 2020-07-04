    url = 'https://coinmarketcap.com/all/views/all'
    all_links = get_all_links(get_html(url))
    
    with Pool(40) as p:
        p.map(make_all, all_links)
    
    end = datetime.now()
    total = end - start
    print(str(total))
    a = input()


if __name__ == '__main__':
     main()