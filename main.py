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
car_number, seria, tex_number = 'car_number', 'seria', 'tex_number'

asyncio.run(login(main_link, username, password, region, car_number, seria, tex_number))

