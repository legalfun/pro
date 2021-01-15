
    def crop(self, location, size):
        image = Image.open('avito_screenshot.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        image.crop((x, y, x+width, y+height)).save('tel.gif')
        self.tel_recon()

    def navigate(self):
        self.driver.get('https://www.avito.ru/velikie_luki/telefony/lenovo_a319_1161088336')
        button = self.driver.find_element_by_xpath(
            '//button[@class="button item-phone-button js-item-phone-button 
button-origin button-origin-blue button-origin_full-width 
button-origin_large-extra item-phone-button_hide-phone 
item-phone-button_card js-item-phone-button_card"]')
        button.click()

        sleep(3)

        self.take_screenshot()

        image = self.driver.find_element_by_xpath(
            '//div[@class="item-phone-big-number js-item-phone-big-number"]//*')
        location = image.location
        size = image.size

        self.crop(location, size)


def main():
    b = Bot()


if __name__ == '__main__':
    main()