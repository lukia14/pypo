from service.ItemService import ItemService

class ItemController:
    def __init__(self):
        pass

    def loja(self):
        oItemService = ItemService()
        return oItemService.loja()

    def apiItensLoja(self):
        oItemService = ItemService()
        return oItemService.apiItensLoja()
    
    def apiEstoque(self):
        oItemService = ItemService()
        return oItemService.apiEstoque()
    
    def apiSalvarCompra(self):
        oItemService = ItemService()
        return oItemService.apiSalvarCompra()