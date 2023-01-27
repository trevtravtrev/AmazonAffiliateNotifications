import json


def search_json_category(json_file, category):
    with open(json_file, "r") as f:
        data = json.load(f)

    for key in data:
        if category in key:
            return float(data[key]["percentage"].strip('%'))/100
        # if the category isn't found
        else:
            continue
    return float(data["All Other Categories"]["percentage"].strip('%'))/100



if __name__ == '__main__':
    json_file = "commissions.json"
    print(search_json_category(json_file, "Kitchen & Dining"))
    print(search_json_category(json_file, "Clothing & Accessories"))
    print(search_json_category(json_file, "Health & Household"))
    print(search_json_category(json_file, "Beauty & Grooming"))
    print(search_json_category(json_file, "Shoes, Handbags, Wallets, Sunglasses"))
    print(search_json_category(json_file, "Automotive"))
    print(search_json_category(json_file, "Luxury Beauty"))
    print(search_json_category(json_file, "Grocery & Gourmet Food"))
    print(search_json_category(json_file, "zzzz"))
