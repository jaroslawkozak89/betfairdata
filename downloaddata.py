import betfairlightweight

trading = betfairlightweight.APIClient("katarzynagasienica1@gmail.com","Passwordshouldgohere", app_key="7Y1J88OHOt5f96hV")

trading.login_interactive()

file_list = trading.historic.get_file_list(
    "Soccer", "Basic Plan", 15, 12, 2019, 19, 12, 2019,  market_types_collection=["MATCH_ODDS"],
    countries_collection=['GB'], file_type_collection=['M'])

for file in file_list:
    print(file)
    download = trading.historic.download_file(file_path=file)
    print(download)