# from tony import seed_data
# from kfc import seed_data
# from honey import seed_data
# from smash import seed_data
from subway import seed_data

def printSeederData(restaurant_id, starting_item_id, data):
    nl = '\n'
    nt = '\t'
    final_text = ''
    for item in data:
        item_text = f'item{starting_item_id} = Item(name="{item[0]}", description="{item[1]}", price={item[2]}, restaurant_id={restaurant_id},{nl}{nt}image_url="{item[3]}"){nl}db.session.add(item{starting_item_id}){nl}{nl}'
        starting_item_id += 1
        final_text += item_text
    return final_text

print(printSeederData(8, 162, seed_data))