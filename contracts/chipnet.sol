// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ChipNet {
    struct Advertisement {
        uint256 index;
        string title;
        uint256 pricePerHour;
        address payable seller;
        bool active;
    }

    struct Service {
        uint256 index;
        uint256 adIndex;
        uint256 bidIndex;
        string accessLink;
        string password;
        uint256 SOSTimestamp;
        uint256 EOSTimestamp;
        bool active;
    }

    struct Bid {
        uint256 index;
        uint256 adIndex;
        uint256 serviceIndex;
        address payable bidder;
        uint256 noOfHours; // in hours
        bool approved;
        bool active;
    }

    // An array of Advertisement structs
    Advertisement[] private ads;

    // An array of Service structs
    Service[] private services;

    // An array of Bid structs
    Bid[] private bids;

    // create and push a dummy ad to the ads array
    Advertisement initAd = Advertisement({
        title: "",
        index: 0,
        pricePerHour: 0,
        seller: payable(address(0)),
        active: false
    });

    // create a push a dummy service to the services array
    Service initService = Service({
        adIndex: 0,
        bidIndex: 0,
        index: 0,
        accessLink: "",
        password: "",
        SOSTimestamp: 0,
        EOSTimestamp: 0,
        active: false
    });

    // create and push a dummy bid to the bids array
    Bid initBid = Bid({
        adIndex: 0,
        index: 0,
        serviceIndex: 0,
        bidder: payable(address(0)),
        noOfHours: 0,
        approved: false,
        active: false
    });

    // push the dummy ad to the ads array
    constructor() {
        ads.push(initAd);
        services.push(initService);
        bids.push(initBid);
    }

    // A mapping between the creator's address and ads called adsOf
    mapping(address => uint256[]) private adsOf;

    // A mapping between the buyer address and ads called servicesOf
    mapping(address => uint256[]) private servicesOf;

    // A mapping between the bidder address and ads called purchases
    mapping(address => uint256[]) private bidsOf;

    // A function that returns the ads array
    function getAllAds() public view returns (Advertisement[] memory) {
        return ads;
    }

    // A function to get the bids of a user
    function getBidsOf(address _user) public view returns (uint256[] memory) {
        // create a new Bid array
        return bidsOf[_user];
    }

    // A function that returns the number of ads
    function getAdsCount() public view returns (uint256) {
        return ads.length;
    }

    // A function that takes a title and price to post an Advertisement and returns it index
    function postAd(
        string memory _title,
        uint256 _pricePerHour
    ) public returns (uint256) {
        // create a new Advertisement struct
        Advertisement memory ad = Advertisement({
            title: _title,
            index: ads.length,
            pricePerHour: _pricePerHour,
            seller: payable(msg.sender),
            active: true
        });

        // push the Advertisement to the ads array
        ads.push(ad);
        // push the index of the Advertisement to the adsOf mapping
        adsOf[msg.sender].push(ads.length - 1);
        // return the index of the ad
        return ads.length - 1;
    }

    // An event that will be emitted when an ad is purchased
    event newBid(uint256 bidIndex);

    // A function that takes an ad index and a number of hours to create a new Bid and returns it index and is payable
    function bidOnAd(uint256 _adIndex, uint256 _noOfHours) public payable returns (uint256) {
        // get the Advertisement from the ads array
        Advertisement memory ad = ads[_adIndex];

        // require that the Advertisement is active
        require(ad.active == true, "Advertisement is inactive");

        // require that the caller is not the seller
        require(msg.sender != ad.seller, "Seller cannot bid on their own ad");

        // require that the value sent is equal to the price of the ad
        require(msg.value == ad.pricePerHour * _noOfHours, "Value sent is not equal to the price of the ad");

        // create a new Bid struct
        Bid memory bid = Bid({
            adIndex: _adIndex,
            index: bids.length,
            serviceIndex: 0,
            bidder: payable(msg.sender),
            noOfHours: _noOfHours,
            approved: false,
            active: true
        });

        // push the Bid to the bids array
        bids.push(bid);
        // push the index of the Bid to the bidsOf mapping
        bidsOf[msg.sender].push(bids.length - 1);
        // emit the newBid event
        emit newBid(bids.length - 1);
        // return the index of the bid
        return bids.length - 1;
    }


    // A function to make a bid inactive and return the money to the bidder
    function cancelBid(uint256 _bidIndex) public {
        // get the Bid from the bids array
        Bid memory bid = bids[_bidIndex];

        // require that the caller is the bidder
        require(msg.sender == bid.bidder, "Only bidder can cancel bid");

        // require that the bid is active
        require(bid.active == true, "Bid is already inactive");

        // require that the bid is not approved
        require(bid.approved == false, "Bid is already approved");

        // set the bid to inactive
        bids[_bidIndex].active = false;

        // transfer the money back to the bidder
        payable(msg.sender).transfer(bid.noOfHours * ads[bid.adIndex].pricePerHour);
    }

    // A function that creates a new service instance and returns its index. It's arguments are the bid, access link, password, password
    function createService(uint256 _bidIndex) public returns (uint256) {
        // get the Bid from the bids array
        Bid memory bid = bids[_bidIndex];

        // get the Advertisement from the ads array
        Advertisement memory ad = ads[bid.adIndex];

        // require that the Bid is approved
        require(bid.approved == true, "Bid is not approved");

        // require that the caller is the seller
        require(msg.sender == ad.seller, "Only seller can create service instance");

        // create a new Service struct
        Service memory service = Service({
            adIndex: bid.adIndex,
            bidIndex: _bidIndex,
            index: services.length,
            accessLink: "",
            password: "",
            SOSTimestamp: 0,
            EOSTimestamp: 0,
            active: true
        });

        // push the Service to the services array
        services.push(service);
        // push the index of the Service to the servicesOf mapping
        servicesOf[msg.sender].push(services.length - 1);
        // return the index of the service
        return services.length - 1;
    }

    // an event that will be emitted when a bid is approved
    event bidApproved(uint256 bidIndex);

    // A function that takes a Bid index and approves it and returns the index of the Service instance
    function approveBid(uint256 _bidIndex) public returns (uint256) {
        // get the Bid from the bids array
        Bid memory bid = bids[_bidIndex];

        // get the Advertisement from the ads array
        Advertisement memory ad = ads[bid.adIndex];

        // require that the caller is the seller
        require(msg.sender == ad.seller, "Only seller can approve bid");

        // require that the Bid is not approved
        require(bid.approved == false, "Bid is already approved");

        // require that the Bid is active
        require(bid.active == true, "Bid is inactive");

        // make the Bid approved
        bids[_bidIndex].approved = true;

        // create a new Service struct
        Service memory service = Service({
            adIndex: bid.adIndex,
            bidIndex: _bidIndex,
            index: services.length,
            accessLink: "",
            password: "",
            SOSTimestamp: 0,
            EOSTimestamp: 0,
            active: true
        });

        // make the bid inactive
        bids[_bidIndex].active = false;

        // push the Service to the services array
        services.push(service);
        // push the index of the Service to the servicesOf mapping
        servicesOf[msg.sender].push(services.length - 1);
        // emit the bidApproved event
        emit bidApproved(_bidIndex);
        // return the index of the service
        return services.length - 1;
    }

    // create a function that posts the access link and password to the service instance
    function postCredentials(uint256 _serviceIndex, string memory _accessLink, string memory _password) public {
        // get the Service from the services array
        Service memory service = services[_serviceIndex];

        // get the Bid from the bids array
        Bid memory bid = bids[service.bidIndex];

        // get the Advertisement from the ads array
        Advertisement memory ad = ads[bid.adIndex];

        // require that the caller is the seller
        require(msg.sender == ad.seller, "Only seller can post access link");

        // require that the Service is active
        require(service.active == true, "Service is already inactive");

        // require that the Service has not yet started
        require(service.SOSTimestamp == 0, "Service has not started");

        // require that the access link is not empty
        require(bytes(_accessLink).length > 0, "Access link cannot be empty");

        // require that the password is not empty
        require(bytes(_password).length > 0, "Password cannot be empty");

        // set the access link
        services[_serviceIndex].accessLink = _accessLink;

        // set the password
        services[_serviceIndex].password = _password;

        // set the start of service timestamp
        services[_serviceIndex].SOSTimestamp = block.timestamp;

        // set the end of service timestamp
        services[_serviceIndex].EOSTimestamp = block.timestamp + (bid.noOfHours * 1 hours);
    }


    // create a function that ends the service instance and returns the money to the seller
    function endService(uint256 _serviceIndex) public {
        // get the Service from the services array
        Service memory service = services[_serviceIndex];

        // get the Bid from the bids array
        Bid memory bid = bids[service.bidIndex];

        // get the Advertisement from the ads array
        Advertisement memory ad = ads[bid.adIndex];

        // require that the caller is the seller
        require(msg.sender == ad.seller, "Only seller can end service");

        // require that the Service is active
        require(service.active == true, "Service is already inactive");

        // require that the Service has started
        require(service.SOSTimestamp > 0, "Service has not started");

        // require that the Service has not ended
        require(service.EOSTimestamp > block.timestamp, "Service has already ended");

        // set the end of service timestamp
        services[_serviceIndex].EOSTimestamp = block.timestamp;

        // set the service to inactive
        services[_serviceIndex].active = false;

        // transfer the money to the seller
        payable(ad.seller).transfer(bid.noOfHours * ad.pricePerHour);
    }
}
