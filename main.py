import asyncio

from playwright.async_api import async_playwright


async def login(
        main_link: str,
        username: str,
        password: str,
        region: str,
        car_number: str,
        seria: str,
        tex_number: str
):
    async with async_playwright() as playwright:
        timeout = 3000
        browser = await playwright.chromium.launch(headless=True, timeout=timeout)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(main_link)
        await page.get_by_role("link", name="Kirish").click()
        await page.get_by_label("Login", exact=True).fill(username)
        await page.get_by_label("Parol").fill(password)
        await page.get_by_role('button', name='Kirish').click()
        await page.get_by_role('link', name='Xizmatdan foydalanish', exact=True).click()
        await page.get_by_role("button", name="Keyingisi").click()

        if await page.get_by_label("Avtotransport vositasi ro‘yxatdan o‘tgan hududni tanlang").count():
            await page.get_by_label("Avtotransport vositasi ro‘yxatdan o‘tgan hududni tanlang").select_option(region)
            await page.get_by_role("button", name="Keyingisi").click()
        await page.get_by_label("Avtotransport davlat raqami belgisi").fill(car_number)
        await page.get_by_label("Texnik pasport seriyasi").fill(seria)
        await page.get_by_label("Texnik pasport raqami").fill(tex_number)
        await page.get_by_role("button", name="Keyingisi").click()
        if await page.get_by_label("Avtotransport davlat raqami belgisi").count():
            help_text = await page.inner_html(".help-block")
            app_id = help_text
            print(app_id)
        else:
            page_locator = page.locator("table#w0")
            table_text = await page_locator.inner_text()
            print(table_text)
        await context.close()
        await browser.close()


main_link = "https://my.gov.uz/oz/service/415"
username = 'user'
password = 'password'
region = 'Toshkent shahri'
car_number, seria, tex_number = '01G408JB', 'AAF', '1713736'

asyncio.run(login(main_link, username, password, region, car_number, seria, tex_number))

"""
 01G408JB  | 1713736       | AAF
 40K583LA  | 0399164       | AAF
 01W790YA  | 0033408       | AAF
 01Z177NA  | 1426786       | AAF
 01626QGA  | 1859259       | AAF
 01402DFA  | 7453516       | AAC
 10Y760KA  | 4961127       | AAC
 01J117DB  | 0476916       | AAF
 30071TTF  | 6753967       | AAC
 01K510WA  | 6262147       | AAC
 01W220FB  | 1296820       | AAF
 01C017TA  | 5400499       | AAC
 40B168SA  | 1541769       | AAF
 10Q003SA  | 1569662       | AAF
 95470TAA  | 6904182       | AAC
 10Y049BB  | 1326470       | AAG
 01M736ZB  | 1090207       | AAG
 01655BGA  | 0765057       | AAF
 01D504KB  | 1904866       | AAF
 01H001200 | 2836764       | AAC
 01211VSB  | 2150669       | AAF
 80E661PA  | 1585852       | AAF
 01H141DA  | 0204020       | AAE
 010511AA  | 0786685       | AAF
 70J728LA  | 6838376       | AAC
 90Z780KA  | 0067060       | AAF
 95F772KA  | 2755770       | AAF
 01E088MB  | 2425878       | AAF
 01H328YA  | 0896527       | AAF
 30M445VA  | 2740776       | AAF
 70T444AA  | 2133581       | AAF
 60757RAA  | 1101224       | AAF
 01A799YA  | 6777847       | AAC
 01T793KB  | 2058737       | AAF
 90Y373MA  | 2528837       | AAF
 75A938JA  | 7286395       | AAC
"""
