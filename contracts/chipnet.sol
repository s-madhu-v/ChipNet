// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ChipNet {
    struct Advertisement {
        string title;
        uint256 price;
        address payable seller;
        bool active;
    }

    // A struct for purchases of computing power
    struct Purchase {
        uint256 adIndex;
        address payable buyer;
        // string tcpAddress;
        // uint256 port;
    }

    // An array of Advertisement structs
    Advertisement[] public ads;

    // An array of Purchase structs
    Purchase[] public purchases;

    // A function that returns the number of ads
    function getAdsCount() public view returns (uint256) {
        return ads.length;
    }

    // A function that returns an ad at an index
    function getAd(
        uint256 _index
    ) public view returns (string memory, uint256, address, bool) {
        Advertisement memory ad = ads[_index];
        return (ad.title, ad.price, ad.seller, ad.active);
    }

    // A function that takes a title and price to post an Advertisement
    function postAd(string memory _title, uint256 _price) public {
        // create a new Advertisement struct
        Advertisement memory ad = Advertisement({
            title: _title,
            price: _price,
            seller: payable(msg.sender),
            active: true
        });

        // push the Advertisement to the ads array
        ads.push(ad);
    }

    // An event that will be emitted when an ad is purchased
    event AdPurchased(uint256 adIndex, uint256 purchaseIndex);

    // A function that takes an Advertisement and buyer address and transfers money to seller
    function purchaseAd(uint256 _adIndex) public payable {
        // get the Advertisement from the ads array
        Advertisement memory ad = ads[_adIndex];

        // require that the Advertisement is active
        require(ad.active == true, "Advertisement is not active");

        // require that the buyer has enough money
        require(msg.value >= ad.price, "Not enough money");

        // require that the buyer is not the seller
        require(msg.sender != ad.seller, "Buyer cannot be seller");

        // transfer money to seller
        ad.seller.transfer(msg.value);

        // create a new Purchase struct
        Purchase memory purchase = Purchase({
            adIndex: _adIndex,
            buyer: payable(msg.sender)
            // tcpAddress: _tcpAddress,
            // port: _port
        });

        // push the Purchase to the purchases array
        purchases.push(purchase);

        // emit the AdPurchased event
        emit AdPurchased(_adIndex, purchases.length - 1);
    }
}
