from bs4 import BeautifulSoup
import requests

ZILLOW_LINK = 'https://appbrewery.github.io/Zillow-Clone/'


class Rent:
    """This is a model for a rent."""

    def __init__(self, rent_address, rent_link, rent_price):
        self.address = rent_address
        self.price = rent_price
        self.link = rent_link


class DataPuller:
    """This class has the goal to extract the necessary data from Zillow website clone."""

    def __init__(self):
        zillow_response = requests.get(ZILLOW_LINK).text
        self.soup = BeautifulSoup(zillow_response, 'html.parser')
        self.price_list = self.extract_the_pricing()
        self.rent_link_list = self.get_links()
        self.address_list = self.extract_the_address()
        self.rent_qty = len(self.price_list)

    def extract_the_pricing(self):
        list_of_tag_prices = self.soup.find_all('span', class_='PropertyCardWrapper__StyledPriceLine')
        list_of_rent_prices = [tag.get_text(strip=True) for tag in list_of_tag_prices]
        final_list = [price.split('+')[0] if '+' in price else price.split('/')[0] for price in list_of_rent_prices]
        return final_list

    def extract_the_address(self):
        list_of_address_tags = self.soup.find_all('address', attrs={'data-test': 'property-card-addr'})
        list_of_rent_address = [tag.get_text(strip=True) for tag in list_of_address_tags]
        cleaned_list_address = [address.split('|')[1] if '|' in address else address for address in
                                list_of_rent_address]
        return cleaned_list_address

    def get_links(self):
        tag_link_list = self.soup.find_all('a', class_='property-card-link')
        links_list = [tag['href'] for tag in tag_link_list]
        return links_list

    def get_rent_list(self):
        available_rents = [
            Rent(rent_address=self.address_list[i], rent_link=self.rent_link_list[i], rent_price=self.price_list[i])
            for i in range(self.rent_qty)]
        return available_rents
