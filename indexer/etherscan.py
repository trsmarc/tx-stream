import requests
from decouple import config
from event_parser import ResponseParser as parser


def get_latest_block_number() -> str:
    """Returns the latest block number."""

    url = (
        f'{config("ETHERSCAN_API_URL")}'
        'module='
        'proxy'
        '&action='
        'eth_blockNumber'
        '&apikey='
        f'{config("ETHERSCAN_API_KEY")}'
    )

    r = requests.get(url, headers={"User-Agent": ""})
    return parser.parse(r)


def get_filtered_event_logs(
    contract_addr: str,
    from_block: str,
    to_block: str,
    topic: str,
    page: str,
    event_offset: str,
) -> str:
    """Returns event logs by address filtered by topics."""

    url = (
        f'{config("ETHERSCAN_API_URL")}'
        'module='
        'logs'
        '&action='
        'getLogs'
        '&fromBlock='
        f'{from_block}'
        '&toBlock='
        f'{to_block}'
        '&address='
        f'{contract_addr}'
        '&topic0='
        f'{topic}'
        '&page='
        f'{page}'
        '&offset='
        f'{event_offset}'
        '&apikey='
        f'{config("ETHERSCAN_API_KEY")}'
    )

    r = requests.get(url, headers={"User-Agent": ""})
    return parser.parse(r)
