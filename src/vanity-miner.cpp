#include <algorithm>
#include <string>
#include <bitcoin/bitcoin.hpp>

const std::string search = "1kid";
bc::ec_secret random_secret(std::default_random_engine &engine);
std::string bitcoin_address(const bc::ec_secret &secret);
bool match_found(const std::string &address);

int main(int argc, char *argv[])
{
    std::random_device random;
    std::default_random_engine engine(random());

    while (true)
    {
        bc::ec_secret secret = random_secret(engine);
        std::string address = bitcoin_address(secret);
        if (match_found(address))
        {
            std::cout << "Found vanity address! " << address << std::endl;
            std::cout << "Secret: " << bc::encode_base16(secret) << std::endl;
            return EXIT_SUCCESS;
        }
    }

    return EXIT_SUCCESS;
}

bc::ec_secret random_secret(std::default_random_engine &engine)
{
    bc::ec_secret secret;
    for (uint8_t &byte : secret)
    {
        byte = engine() % std::numeric_limits<uint8_t>::max();
    }
    return secret;
}

std::string bitcoin_address(const bc::ec_secret &secret)
{
    bc::ec_compressed public_key;
    bc::secret_to_public(public_key, secret);
    bc::wallet::payment_address address(public_key);
    return address.encoded();
}

bool match_found(const std::string &address)
{
    auto addr_it = address.begin();
    for (auto it = search.begin(); it != search.end(); ++it, ++addr_it)
    {
        if (*it != std::tolower(*addr_it))
        {
            return false;
        }
    }
    return true;
}