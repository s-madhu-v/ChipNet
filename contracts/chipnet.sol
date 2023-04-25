// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ChipNet {
    struct Advertisement {
        uint256 index;
        string title;
        string processingPower;
        uint256 coresAllocation;
        string memoryAllocation;
        string storageAllocation;
        uint256 pricePerHour;
        address payable seller;
        bool active;
    }

    struct Service {
        uint256 index;
        uint256 adIndex;
        uint256 bidIndex;
        uint256 serviceIndex;
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
        uint256 noOfHours;
        string publicKey;
        bool approved;
        bool active;
    }

    Advertisement[] private ads;

    function getAd(uint256 _index) public view returns (Advertisement memory) {
        return ads[_index];
    }

    Service[] private services;

    function getService(uint256 _index) public view returns (Service memory) {
        return services[_index];
    }

    Bid[] private bids;

    function getBid(uint256 _index) public view returns (Bid memory) {
        return bids[_index];
    }

    Advertisement initAd =
        Advertisement({
            title: "",
            index: 0,
            pricePerHour: 0,
            seller: payable(address(0)),
            active: false,
            coresAllocation: 0,
            memoryAllocation: "0g",
            storageAllocation: "0G",
            processingPower: "0 GHz"
        });

    Service initService =
        Service({
            adIndex: 0,
            bidIndex: 0,
            index: 0,
            serviceIndex: 0,
            accessLink: "",
            password: "",
            SOSTimestamp: 0,
            EOSTimestamp: 0,
            active: false
        });

    Bid initBid =
        Bid({
            adIndex: 0,
            index: 0,
            serviceIndex: 0,
            bidder: payable(address(0)),
            noOfHours: 0,
            publicKey: "",
            approved: false,
            active: false
        });

    constructor() {
        //ads.push(initAd);
        //services.push(initService);
        //bids.push(initBid);
    }

    mapping(address => uint256[]) private adsOf;

    mapping(address => uint256[]) private servicesOf;

    mapping(address => uint256[]) private bidsOf;

    mapping(address => uint256[]) private ordersOf;

    function getAllAds() public view returns (Advertisement[] memory) {
        return ads;
    }

    function getAllServices() public view returns (Service[] memory) {
        return services;
    }

    function getAllBids() public view returns (Bid[] memory) {
        return bids;
    }

    // A function called adsOf that returns the ad structs array corresponding to a user
    function getAdsOf(
        address _user
    ) public view returns (Advertisement[] memory) {
        uint256[] memory adIndices = adsOf[_user];
        Advertisement[] memory yourAds = new Advertisement[](adIndices.length);
        for (uint256 i = 0; i < adIndices.length; i++) {
            yourAds[i] = ads[adIndices[i]];
        }
        return yourAds;
    }

    // A function called bidsOf that returns the bid structs array corresponding to a user
    function getBidsOf(address _user) public view returns (Bid[] memory) {
        uint256[] memory bidIndices = bidsOf[_user];
        Bid[] memory yourBids = new Bid[](bidIndices.length);
        for (uint256 i = 0; i < bidIndices.length; i++) {
            yourBids[i] = bids[bidIndices[i]];
        }
        return yourBids;
    }

    // A function called servicesOf that returns the service structs array corresponding to a user
    function getServicesOf(
        address _user
    ) public view returns (Service[] memory) {
        uint256[] memory serviceIndices = servicesOf[_user];
        Service[] memory yourServices = new Service[](serviceIndices.length);
        for (uint256 i = 0; i < serviceIndices.length; i++) {
            yourServices[i] = services[serviceIndices[i]];
        }
        return yourServices;
    }

    // A function called ordersOf that returns the service structs array corresponding to a user
    function getOrdersOf(address _user) public view returns (Service[] memory) {
        uint256[] memory serviceIndices = ordersOf[_user];
        Service[] memory yourOrders = new Service[](serviceIndices.length);
        for (uint256 i = 0; i < serviceIndices.length; i++) {
            yourOrders[i] = services[serviceIndices[i]];
        }
        return yourOrders;
    }

    function getAdsCount() public view returns (uint256) {
        return ads.length;
    }

    function postAd(
        string memory _title,
        string memory _processingPower,
        uint256 _coresAllocation,
        string memory _memoryAllocation,
        string memory _storageAllocation,
        uint256 _pricePerHour
    ) public returns (uint256) {
        Advertisement memory ad = Advertisement({
            title: _title,
            processingPower: _processingPower,
            coresAllocation: _coresAllocation,
            memoryAllocation: _memoryAllocation,
            storageAllocation: _storageAllocation,
            index: ads.length,
            pricePerHour: _pricePerHour,
            seller: payable(msg.sender),
            active: true
        });

        ads.push(ad);
        adsOf[msg.sender].push(ads.length - 1);
        return ads.length - 1;
    }

    event newBid(uint256 bidIndex, uint256 adIndex);

    function bidOnAd(
        uint256 _adIndex,
        uint256 _noOfHours,
        string memory _pubKey
    ) public payable returns (uint256) {
        Advertisement memory ad = ads[_adIndex];

        require(ad.active == true, "Advertisement is inactive");

        require(msg.sender != ad.seller, "Seller cannot bid on their own ad");

        require(
            msg.value == ad.pricePerHour * _noOfHours,
            "Value sent is not equal to the price of the ad"
        );

        Bid memory bid = Bid({
            adIndex: _adIndex,
            index: bids.length,
            serviceIndex: 0,
            bidder: payable(msg.sender),
            noOfHours: _noOfHours,
            publicKey: _pubKey,
            approved: false,
            active: true
        });

        bids.push(bid);
        bidsOf[msg.sender].push(bids.length - 1);
        emit newBid(bids.length - 1, _adIndex);
        return bids.length - 1;
    }

    function cancelBid(uint256 _bidIndex) public {
        Bid memory bid = bids[_bidIndex];
        require(msg.sender == bid.bidder, "Only bidder can cancel bid");
        require(bid.active == true, "Bid is already inactive");
        require(bid.approved == false, "Bid is already approved");
        bids[_bidIndex].active = false;
        payable(msg.sender).transfer(
            bid.noOfHours * ads[bid.adIndex].pricePerHour
        );
    }

    event bidApproved(uint256 bidIndex, uint256 serviceIndex);

    function approveBid(uint256 _bidIndex) public returns (uint256) {
        Bid memory bid = bids[_bidIndex];
        Advertisement memory ad = ads[bid.adIndex];
        require(msg.sender == ad.seller, "Only seller can approve bid");
        require(bid.approved == false, "Bid is already approved");
        require(bid.active == true, "Bid is inactive");
        bids[_bidIndex].approved = true;
        Service memory service = Service({
            adIndex: bid.adIndex,
            bidIndex: _bidIndex,
            index: services.length,
            serviceIndex: services.length,
            accessLink: "",
            password: "",
            SOSTimestamp: 0,
            EOSTimestamp: 0,
            active: true
        });

        bids[_bidIndex].active = false;
        ads[bid.adIndex].active = false;
        services.push(service);
        servicesOf[msg.sender].push(services.length - 1);
        ordersOf[bid.bidder].push(services.length - 1);
        emit bidApproved(_bidIndex, services.length - 1);
        return services.length - 1;
    }

    function postCredentials(
        uint256 _serviceIndex,
        string memory _accessLink,
        string memory _password
    ) public {
        Service memory service = services[_serviceIndex];
        Bid memory bid = bids[service.bidIndex];
        Advertisement memory ad = ads[bid.adIndex];
        require(msg.sender == ad.seller, "Only seller can post access link");
        require(service.active == true, "Service is already inactive");
        require(service.SOSTimestamp == 0, "Service has not started");
        require(bytes(_accessLink).length > 0, "Access link cannot be empty");
        require(bytes(_password).length > 0, "Password cannot be empty");
        services[_serviceIndex].accessLink = _accessLink;
        services[_serviceIndex].password = _password;
        services[_serviceIndex].SOSTimestamp = block.timestamp;
        services[_serviceIndex].EOSTimestamp =
            block.timestamp +
            (bid.noOfHours * 1 hours);
    }

    function endService(uint256 _serviceIndex) public {
        Service memory service = services[_serviceIndex];
        Bid memory bid = bids[service.bidIndex];
        Advertisement memory ad = ads[bid.adIndex];
        require(msg.sender == ad.seller, "Only seller can end service");
        require(service.active == true, "Service is already inactive");
        require(service.SOSTimestamp > 0, "Service has not started");
        require(
            service.EOSTimestamp > block.timestamp,
            "Service has already ended"
        );
        services[_serviceIndex].EOSTimestamp = block.timestamp;
        services[_serviceIndex].active = false;
        payable(ad.seller).transfer(bid.noOfHours * ad.pricePerHour);
    }
}
