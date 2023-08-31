from pages.basePage import BasePage
from elements.webElements import WebElements


class CardPage(BasePage):

    def __init__(self, driver):
        self.url = 'https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363'
        super().__init__(driver, self.url)

        self.btn_like = WebElements('button.desctop-usq1f1', driver)



