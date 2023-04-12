// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ChipNet {
    struct Advertisement {
        string title;
        uint256 price;
        address payable seller;
        bool active;
    }

    // An array of Advertisement structs
    Advertisement[] public ads;

    // A mapping between the buyer address and the ad index called purchases
    mapping(address => uint256) public purchases;

    // A function that returns the number of ads
    function getAdsCount() public view returns (uint256) {
        return ads.length;
    }

    // A function that returns an ad at an index
    function getAd(uint256 _index) public view returns (Advertisement memory) {
        return ads[_index];
    }

    // A function that takes a title and price to post an Advertisement and returns it index
    function postAd(
        string memory _title,
        uint256 _price
    ) public returns (uint256) {
        // create a new Advertisement struct
        Advertisement memory ad = Advertisement({
            title: _title,
            price: _price,
            seller: payable(msg.sender),
            active: true
        });

        // push the Advertisement to the ads array
        ads.push(ad);
        // return the index of the ad
        return ads.length - 1;
    }

    // An event that will be emitted when an ad is purchased
    event AdPurchased(uint256 adIndex);

    // A function that takes an Advertisement and buyer address and transfers money to seller and returns purchase index
    function purchaseAd(uint256 _adIndex) public payable returns (uint256) {
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

        // set the Advertisement to inactive
        ads[_adIndex].active = false;

        // set the buyer address to the purchases mapping
        purchases[msg.sender] = _adIndex;

        // emit the AdPurchased event
        emit AdPurchased(_adIndex);
        // return the index of the purchase
        return _adIndex;
    }
}
