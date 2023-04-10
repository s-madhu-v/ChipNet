// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ChipNet {
    struct Advertisement {
        string title;
        string description;
        uint256 price;
        address payable seller;
        bool active;
    }

    // An array of Advertisement structs
    Advertisement[] public ads;

    // A function that returns the number of ads
    function getAdsCount() public view returns (uint256) {
        return ads.length;
    }

    // Get an ad at an index
    function getAd(
        uint256 _index
    )
        public
        view
        returns (string memory, string memory, uint256, address, bool)
    {
        Advertisement memory ad = ads[_index];
        return (ad.title, ad.description, ad.price, ad.seller, ad.active);
    }

    // A function that takes a title, description, and price to post an Advertisement
    function postAd(
        string memory _title,
        string memory _description,
        uint256 _price
    ) public {
        // create an Advertisement struct
        Advertisement memory ad = Advertisement({
            title: _title,
            description: _description,
            price: _price,
            seller: payable(msg.sender),
            active: true
        });

        // push the Advertisement to the ads array
        ads.push(ad);
    }

    // An event that will be emitted when an ad is purchased
    event AdPurchased(
        uint256 index,
        address seller,
        address buyer,
        uint256 price
    );

    // A function to emit an AdPurchased event while also enforcing some rules
    function onAdPurchased(
        uint256 _index,
        address _seller,
        address _buyer,
        uint256 _price
    ) internal {
        // emit the AdPurchased event
        emit AdPurchased(_index, _seller, _buyer, _price);
    }

    // A function that takes an Advertisement and buyer address and transfers money to seller
    function buy(uint256 _index) public payable {
        // get the Advertisement from the ads array
        Advertisement storage ad = ads[_index];

        // require that the Advertisement is active
        require(ad.active == true, "Advertisement is not active");

        // require that the buyer has enough money
        require(msg.value >= ad.price, "Not enough money");

        // require that the buyer is not the seller
        require(msg.sender != ad.seller, "You cannot buy your own ad");

        // transfer money to the seller
        ad.seller.transfer(msg.value);

        // deactivate the Advertisement
        ad.active = false;

        // emit the AdPurchased event
        emit AdPurchased(_index, ad.seller, msg.sender, ad.price);
    }
}
