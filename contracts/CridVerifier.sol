// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract CridVerifier {
    address public owner;
    
    mapping(bytes32 => mapping(bytes32 => bytes32)) public cridHashes;

    event CridRegistered(bytes32 indexed dre, bytes32 indexed semester, bytes32 documentHash);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Apenas o dono do contrato pode chamar esta funcao");
        _;
    }

    function registerCrid(bytes32 dre, bytes32 semester, bytes32 documentHash) public onlyOwner {
        cridHashes[dre][semester] = documentHash;
        emit CridRegistered(dre, semester, documentHash);
    }

    function verifyCrid(bytes32 dre, bytes32 semester, bytes32 documentHash) public view returns (bool) {
        return cridHashes[dre][semester] == documentHash;
    }
}