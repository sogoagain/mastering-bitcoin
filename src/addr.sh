clang++ -std=gnu++11 -o addr addr.cpp -I /opt/homebrew/Cellar/boost@1.76/1.76.0_1/include -L /opt/homebrew/Cellar/boost@1.76/1.76.0_1/lib $(pkg-config --cflags --libs libbitcoin)
