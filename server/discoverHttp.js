const configENV = require('dotenv').config()
config = configENV.parsed;
console.log("config", config)
const fetch = require('node-fetch');
var querystring = require('querystring');

module.exports = class DiscoverHttp {
  constructor() {
    this.domian = 'https://api.discover.com/'
    this.tokenURL = 'https://apis.discover.com/auth/oauth/v2/token'
    this.ENDPOINT = {
      EXCHANGE_RATE: 'dci/currencyconversion/v1/exchangerate',
      CITY_GUIDE: 'cityguides/v2/merchants'
    }

    this.HEADER_PLAN = {
      'EXCHANGE_RATE': 'DCI_CURRENCYCONVERSION_SANDBOX',
      'CITY_GUIDE': 'CITYGUIDES_SANDBOX'

    }

    this.authToken = '6345ffbb-7953-4f67-90b8-2b98b7a4bc09';
    this.scope = 'CITYGUIDES DCIOFFERS DCIOFFERS_POST DCILOUNGES DCILOUNGES_POST DCILOUNGES_PROVIDER_LG DCILOUNGES_PROVIDER_DCIPL DCI_ATM DCI_CURRENCYCONVERSION DCI_CUSTOMERSERVICE DCI_TIP'

   }

  getAPIKey(){
    return config.DISCOVER_APP_API_KEY;
  }
  getBearToken(){
    const tokenAPIKey = config.DISCOVER_APP_API_KEY
    const tokenAPISecret =config.DISCOVER_APP_API_SECRET
    console.log("\n" + `${tokenAPIKey}:${tokenAPISecret}` + "\n")
    const auth = 'Basic ' + Buffer.from(`${tokenAPIKey}:${tokenAPISecret}`).toString('base64');

    const headers = {"Content-Type": 'application/x-www-form-urlencoded', "Authorization": auth }
    console.log("headers", headers)
    var postData = querystring.stringify({
      grant_type: "client_credentials",
      scope:  this.scope
    });
    return this.postData(this.tokenURL, postData, headers);
  }


  async getExchangeRate(currencycd){
    if(!this.authToken){
      this.authToken = await this.getBearToken().then(x => {console.log("getBearToken", x); return x.access_token;});
      console.log("token", this.authToken)
      if(!this.authToken){
        return;
      }
    }
    const url = this.domian + this.ENDPOINT.EXCHANGE_RATE + "?currencycd=" + currencycd;
    const headers = {"X-DFS-API-PLAN": this.HEADER_PLAN.EXCHANGE_RATE, "Authorization": "Bearer " + this.authToken }

    return this.getData(url, headers )
  }


  async getCityGuide(cityname) {
    if(!this.authToken){
      this.authToken = await this.getBearToken().then(x => {console.log("getBearToken", x); return x.access_token;});
      console.log("token", this.authToken)
      if(!this.authToken){
        return;
      }
    }
    const url = this.domian + this.ENDPOINT.CITY_GUIDE + "?merchant_city=" + cityname + "&pagesize=300";
    const headers = {"X-DFS-API-PLAN": this.HEADER_PLAN.CITY_GUIDE, "Authorization": "Bearer " + this.authToken }

    return this.getData(url, headers )
  }

  postData(url, data, extendHeader){
    const allHeader = {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        headers: {
            "Content-Type": "application/json; charset=utf-8",
            ...extendHeader
            // "Content-Type": "application/x-www-form-urlencoded",
        },
        body: data, // body data type must match "Content-Type" header
    };
    // console.log("allHeader", allHeader)

    return fetch(url, allHeader)
    .then(response => {console.log(response); return response.json();});
  }
  getData(url, extendHeader){

    const allHeader = {
        method: "GET", // *GET, POST, PUT, DELETE, etc.
        headers: {
            "Content-Type": "application/json; charset=utf-8",
            ...extendHeader
            // "Content-Type": "application/x-www-form-urlencoded",
        },
    };
    console.log("allHeader", allHeader)

    return fetch(url, allHeader)
    .then(response => response.json());
  }



}
