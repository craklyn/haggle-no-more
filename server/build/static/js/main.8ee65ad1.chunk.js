(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{126:function(e,t,a){e.exports=a.p+"static/media/Map_icon.33ec1984.svg"},127:function(e,t,a){e.exports=a.p+"static/media/DiscoverLogo.e0d6af8a.svg"},131:function(e,t,a){e.exports=a.p+"static/media/Send_Button.afb73dc5.svg"},132:function(e,t,a){e.exports=a.p+"static/media/Check_Button.521df833.svg"},133:function(e,t,a){e.exports=a.p+"static/media/X_Button.a0ab9872.svg"},134:function(e,t,a){e.exports=a.p+"static/media/delete.2a007d0e.svg"},147:function(e,t,a){e.exports=a(278)},152:function(e,t,a){},272:function(e,t,a){},278:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),c=a(76),s=a.n(c),l=(a(152),a(5)),o=a(6),i=a(12),u=a(10),m=a(11),h=a(282),d=a(287),p=a(284),f=(a(32),a(283)),E=a(13),v=a(77),g=a.n(v),_=a(78),b=a.n(_),k=a(79),N=a.n(k),O=function(e){function t(e){var a;return Object(l.a)(this,t),a=Object(i.a)(this,Object(u.a)(t).call(this,e)),console.log(e),a.state={},a}return Object(m.a)(t,e),Object(o.a)(t,[{key:"componentDidMount",value:function(){}},{key:"render",value:function(){var e=this;return r.a.createElement("div",{className:"footerDiv"},r.a.createElement(f.a,{columns:"three",className:"g_footer"},r.a.createElement(f.a.Row,null,r.a.createElement(f.a.Column,{className:"g_icon_column"},r.a.createElement(E.a,{src:b.a,className:"clickableIcon",onClick:function(){e.props.history.push("/place")}})),r.a.createElement(f.a.Column,{className:"g_icon_column"},r.a.createElement(E.a,{src:g.a,className:"clickableIcon",onClick:function(){e.props.history.push("/haggle")}})),r.a.createElement(f.a.Column,{className:"g_icon_column clickableIcon"},r.a.createElement(E.a,{src:N.a})))))}}]),t}(n.Component),y=function(e){function t(){return Object(l.a)(this,t),Object(i.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(o.a)(t,[{key:"render",value:function(){return r.a.createElement("div",null,r.a.createElement(O,null))}}]),t}(n.Component),C=a(280),w=a(84),j=a(30),x=a.n(j),S=a(193).config(),P=function(){function e(){Object(l.a)(this,e),this.domian=window.location.href.indexOf("localhost")>-1?"http://localhost:4200/":"https://anglehackt.appspot.com/",this.ENDPOINT={EXCHANGE_RATE:"exchangerate",CITY_GUIDE:"cityguide"},this.HEADER_PLAN={EXCHANGE_RATE:"DCI_CURRENCYCONVERSION_SANDBOX",CITY_GUIDE:"CITYGUIDES"}}return Object(o.a)(e,[{key:"getBearToken",value:function(){var e=S.DISCOVER_APP_API_KEY,t=S.DISCOVER_APP_API_SECRET,a={"Content-Type":"application/x-www-form-urlencoded",Authorization:"Basic "+btoa("".concat(e,":").concat(t))};return this.postData(this.tokenURL+"grant_type=client_credentials&scope="+this.scope,a)}},{key:"getExchangeRate",value:function(e){var t=this.domian+this.ENDPOINT.EXCHANGE_RATE+"?currencycd="+e,a={"X-DFS-API-PLAN":this.HEADER_PLAN.EXCHANGE_RATE,Authorization:"Bearer "+this.authToken};return console.log("headers",a),this.getData(t,a)}},{key:"getCityGuide",value:function(e){var t=this.domian+this.ENDPOINT.CITY_GUIDE+"?merchant_city="+e,a={"X-DFS-API-PLAN":this.HEADER_PLAN.CITY_GUIDE,Authorization:"Bearer "+this.authToken};return console.log("headers",a),this.getData(t,a)}},{key:"postData",value:function(e,t,a){var n={method:"POST",headers:Object(w.a)({"Content-Type":"application/json; charset=utf-8"},a),body:JSON.stringify(t)};return console.log("allHeader",n),fetch(e,n).then(function(e){return e.json()})}},{key:"getData",value:function(e,t){var a={method:"GET",headers:Object(w.a)({"Access-Control-Allow-Origin":"*","Access-Control-Allow-Headers":"*","Content-Type":"application/json; charset=utf-8"},t)};return x.a.ajax({url:e,type:"GET",headers:a,success:function(e){return e},error:function(e){}})}}]),e}(),A=a(125),D=a.n(A),I=(a(196),a(95),a(126)),T=a.n(I),V=a(127),L=a.n(V),q=a(286),R=a(285),M=function(e){function t(){return Object(l.a)(this,t),Object(i.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(o.a)(t,[{key:"render",value:function(){var e=this.props,t=e.idIter,a=e.m,n=e.locStyle;return r.a.createElement("div",{key:t,style:n,className:"locItem"},r.a.createElement("div",{className:"merchants_row_item"},r.a.createElement("div",null,r.a.createElement("h3",{className:"text_title"},a.name,r.a.createElement("a",{className:"text_title_link",href:a.website},r.a.createElement(q.a,{name:"linkify"})))),r.a.createElement("div",null,"DCI"===a.card_network&&r.a.createElement(E.a,{src:L.a}))),r.a.createElement("div",{className:"merchants_row_item"},r.a.createElement("div",null,r.a.createElement("p",{className:"text_address",style:{maxwidth:"50%"}},a.address1)),r.a.createElement("div",null,r.a.createElement("div",{style:{marginTop:-2}},r.a.createElement("p",{className:"text_address"},"0.1 m")))),r.a.createElement("div",{className:"merchants_row_item"},r.a.createElement("div",null,r.a.createElement("p",{className:"text_address"},a.phone),a.rating>0&&r.a.createElement(R.a,{icon:"star",defaultRating:a.rating,maxRating:5}),a.rating>0&&r.a.createElement("span",null,a.rating)),r.a.createElement("div",null)),r.a.createElement("div",{className:"merchants_row_item"},r.a.createElement("div",null,r.a.createElement("p",{className:"bargin_text"},"Avg. 0 - ",Math.round(30*Math.random()),"% bargaining discount"))))}}]),t}(n.Component),B=function(e){function t(e){var a;return Object(l.a)(this,t),(a=Object(i.a)(this,Object(u.a)(t).call(this,e))).state={currLocs:[],allLocs:[],initLocs:[],curDropVal:"Retail"},a}return Object(m.a)(t,e),Object(o.a)(t,[{key:"getGooglePlaceInformation",value:function(e,t,a){var n=this,r=n.state.initLocs,c=new P,s=c.domian+"googlePlace?query=".concat(t.split(" ").join("+"),"&location=").concat(a[0],",").concat(a[1]);c.domian;x.a.ajax({url:s,type:"GET",success:function(t){var a=x.a.parseJSON(t);if(a.results){for(var c=0;c<a.results.length;c++)if(0===c){r[e].rating=a.results[0].rating||0,r[e].place_id=a.results[0].place_id||"n/a",r[e].reference=a.results[0].reference||"n/a";var s=a.results[0].photos;s&&s.length&&(r[e].photo_reference=s[0].photo_reference)}else{var l={};l.address1=a.results[c].formatted_address?a.results[c].formatted_address.split("Bangkok")[0]:"",l.name=a.results[c].name||0,l.card_network="UnKnown",l.point=[a.results[c].geometry.location.lat,a.results[c].geometry.location.lng],l.mcc=r[0].mcc,l.rating=a.results[c].rating||0,l.place_id=a.results[c].place_id||"n/a",l.reference=a.results[c].reference||"n/a",r.splice(e,0,l)}n.setState({initLocs:r})}return t},error:function(e){}})}},{key:"componentDidMount",value:function(){var e=this,t=new P,a=this;t.getCityGuide("bangkok").then(function(t){return t=JSON.parse(t),e.setState({allLocs:t}),t.result.filter(function(e){return"retail"===e.mcc})}).then(function(t){return e.setState({initLocs:t})}).then(function(e){a.setDataPlaces()})}},{key:"setDataPlaces",value:function(){var e=this,t=this;console.log("x!!!",this.state.currLocs),this.state.initLocs.map(function(e,a){return a>10?e:(console.log("x!!!",a),t.getGooglePlaceInformation(a,e.address1,e.point),e)}),setTimeout(function(){for(var t=e.state.initLocs,a=t.length-1;a>0;a--){var n=Math.floor(Math.random()*(a+1)),r=[t[n],t[a]];t[a]=r[0],t[n]=r[1]}e.setState({currLocs:t})},1500)}},{key:"render",value:function(){var e=this,t=0,a={borderColor:"white"};return r.a.createElement("div",{className:"listPlaces"},r.a.createElement("div",{className:"top",style:{backgroundColor:"#EC6434",width:"100%",height:50,textAlign:"center",color:"white",fontSize:30}},r.a.createElement("p",{className:"topText"},"Bangkok Markets")),r.a.createElement("div",{className:"second_handler"},r.a.createElement("div",{className:"filter",style:{fontSize:25}},r.a.createElement(D.a,{options:[{value:"retail",label:"Retail"},{value:"restaurants",label:"Restaurants"},{value:"hotels",label:"Hotels"}],value:this.state.curDropVal,onChange:function(t){console.log(e.state.allLocs.result);var a=e.state.allLocs.result.filter(function(e){return e.mcc===t.value});e.setState({currLocs:a,curDropVal:t.label}),e.setDataPlaces()},placeholder:"Filter by Merchants"})),r.a.createElement(E.a,{src:T.a,className:"clickableIcon",onClick:function(){return e.props.history.push("/map")}})),r.a.createElement(function(){var n=e.state.currLocs.map(function(e){return t++,r.a.createElement(M,{idIter:t,m:e,locStyle:a})});return r.a.createElement("ul",{className:"metchant_parents"},n)},{style:{padding:"20px",marginBottom:10,border:"solid",borderColor:"#0b3c5d",borderWidth:1,position:"relative",display:"block",listStyleType:"none"}}),r.a.createElement(C.a,null),r.a.createElement("div",null,r.a.createElement(O,this.props)))}}]),t}(n.Component),G=a(23),H=a(281),U=a(131),X=a.n(U),Y=a(132),z=a.n(Y),F=a(133),J=a.n(F),Q=a(134),W=a.n(Q),$=function(e){function t(){var e;return Object(l.a)(this,t),(e=Object(i.a)(this,Object(u.a)(t).call(this))).state={propsedValues:0,convertValues:0,exchange_rate:0,currencycd:"THB",showOffer:!1,reverseOffer:!1,appendClassName:""},e.allButtons=e.getNumbers(),e.offerMake=e.offerMake.bind(Object(G.a)(Object(G.a)(e))),e.rejectOffer=e.rejectOffer.bind(Object(G.a)(Object(G.a)(e))),e}return Object(m.a)(t,e),Object(o.a)(t,[{key:"componentDidMount",value:function(){var e=new P,t=this;e.getExchangeRate(this.state.currencycd).done(function(e){console.log("data.exchange_rate",JSON.parse(e).exchange_rate),t.setState({exchange_rate:JSON.parse(e).exchange_rate})})}},{key:"handleNumber",value:function(e){this.setState({appendClassName:"an_c_ca"});var t=10*this.state.propsedValues+e;console.log("this.state.exchange_rate",this.state.exchange_rate),console.log(t/this.state.exchange_rate),this.setState({propsedValues:t,convertValues:t/this.state.exchange_rate});var a=this;setTimeout(function(){return a.setState({appendClassName:""})},2e3)}},{key:"onHandleAction",value:function(e){if("back"===e){var t=parseInt(this.state.propsedValues/10);this.setState({propsedValues:t,convertValues:t*this.state.exchange_rate})}else"offer"===e&&this.setState({showOffer:!0})}},{key:"getNumbers",value:function(){for(var e=[],t=1;t<10;t++)e.push(t);return e}},{key:"OnPressChangeVal",value:function(e){console.log(e),this.handleNumber(e)}},{key:"offerMake",value:function(){this.props.history.push("/feedback")}},{key:"rejectOffer",value:function(){this.setState({reverseOffer:!this.state.reverseOffer})}},{key:"render",value:function(){var e=this;return r.a.createElement("div",{className:this.state.reverseOffer?"reverseOffer-view":""},this.state.showOffer&&r.a.createElement("div",{className:this.state.reverseOffer?"offer_panel_reverse":"offer_panel"},r.a.createElement("div",{className:"offer_inner"},r.a.createElement("p",{className:"client_view_price",style:{margin:0}},"\u0e3f ",this.state.convertValues.toFixed(2).toLocaleString()),this.state.reverseOffer&&r.a.createElement("p",{className:"client_view_price client_view_price_small",style:{margin:0}},"$ (",this.state.propsedValues.toFixed(2).toLocaleString(),")"),r.a.createElement("div",{className:"group_button"},r.a.createElement("div",{className:"clickableIcon",onClick:this.offerMake},r.a.createElement(E.a,{src:z.a,svgStyle:{width:50}})),r.a.createElement("div",{className:"clickableIcon",onClick:this.rejectOffer},r.a.createElement(E.a,{src:J.a,svgStyle:{width:50}}))))),r.a.createElement("div",{className:this.state.showOffer?"cal_main cal_main_openOffer"+(this.state.reverseOffer?" cal_main_openOffer_reverse":""):"cal_main"},r.a.createElement("div",{className:"cal_main_wrap"},r.a.createElement("div",{className:"cal_display"},r.a.createElement("div",null,r.a.createElement(H.a,{name:"th",svgStyle:{width:25}})),r.a.createElement("p",null,"\u0e3f ",this.state.convertValues.toFixed(2).toLocaleString())),r.a.createElement("div",{className:"cal_display "+this.state.appendClassName},r.a.createElement("div",null,r.a.createElement(H.a,{name:"us",svgStyle:{width:25}})),r.a.createElement("p",null,"$",this.state.propsedValues.toFixed(2).toLocaleString()))),r.a.createElement("div",{style:{display:"flex",justifyContent:"center",marginTop:"40px"}},r.a.createElement("div",{className:""},r.a.createElement("div",{className:"cal_row"},r.a.createElement("p",{className:"letter_square",onClick:function(){return e.OnPressChangeVal(1)}},"1"),r.a.createElement("p",{className:"letter_square",onClick:function(){return e.OnPressChangeVal(2)}},"2"),r.a.createElement("p",{className:"letter_square",onClick:function(){return e.OnPressChangeVal(3)}},"3")),r.a.createElement("div",{className:"cal_row"},r.a.createElement("p",{className:"letter_square",onClick:function(){return e.OnPressChangeVal(4)}},"4"),r.a.createElement("p",{className:"letter_square",onClick:function(){return e.OnPressChangeVal(5)}},"5"),r.a.createElement("p",{className:"letter_square",onClick:function(){return e.OnPressChangeVal(6)}},"6")),r.a.createElement("div",{className:"cal_row"},r.a.createElement("p",{className:"letter_square",onClick:function(){return e.OnPressChangeVal(7)}},"7"),r.a.createElement("p",{className:"letter_square",onClick:function(){return e.OnPressChangeVal(8)}},"8"),r.a.createElement("p",{className:"letter_square",onClick:function(){return e.OnPressChangeVal(9)}},"9")),r.a.createElement("div",{className:"cal_row"},r.a.createElement("p",{className:"letter_square",onClick:function(){return e.onHandleAction(",")}},","),r.a.createElement("p",{className:"letter_square",onClick:function(){return e.OnPressChangeVal(0)}},"0"),r.a.createElement("p",{className:"letter_square",onClick:function(){return e.onHandleAction(".")}},"."))),r.a.createElement("div",{className:"cal_col_test"},r.a.createElement("p",{className:"letter_square",onClick:function(){return e.onHandleAction("back")}},r.a.createElement(E.a,{src:W.a,svgStyle:{width:40}})),r.a.createElement("p",{className:"letter_square letter_icon",onClick:function(){return e.onHandleAction("offer")}},r.a.createElement(E.a,{src:X.a,svgStyle:{width:40}}))))),r.a.createElement(O,this.props))}}]),t}(n.Component),K=function(e){function t(){return Object(l.a)(this,t),Object(i.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(o.a)(t,[{key:"render",value:function(){return r.a.createElement("div",null,r.a.createElement("div",{className:"top",style:{backgroundColor:"#EC6434",width:"100%",height:50,textAlign:"center",color:"white",fontSize:30}},r.a.createElement("p",{className:"topText"},"Bangkok Markets")),r.a.createElement("iframe",{title:"Leaflet map of location with markets marked",src:"https://s3.amazonaws.com/discoverhack/maps/index.html",style:{height:"100%",width:"100%",border:0,margin:0,position:"fixed",overflowY:"hidden"}}),r.a.createElement("div",null,r.a.createElement(O,this.props)))}}]),t}(n.Component),Z=(a(272),function(e){function t(){var e;return Object(l.a)(this,t),(e=Object(i.a)(this,Object(u.a)(t).call(this))).state={questions:[{q:"Did you pay with cash or card?",optionsType:"binary",options:["cash","card"],iconNames:["money bill alternate outline","credit card"]},{q:"How much discount did you receive?",optionsType:"multi",options:["0-30%","30-60%","60-90%"]}],currentQuestions:0},e.onPressSubmit=e.onPressSubmit.bind(Object(G.a)(Object(G.a)(e))),e}return Object(m.a)(t,e),Object(o.a)(t,[{key:"componentDidMount",value:function(){}},{key:"onPressSubmit",value:function(){var e=this.state.currentQuestions+1;e<this.state.questions.length?this.setState({currentQuestions:e}):this.props.history.push("/place")}},{key:"render",value:function(){var e=this,t=this.state.questions[this.state.currentQuestions];return r.a.createElement("div",null,r.a.createElement("div",{className:"top_header"},"Bankok Markets"),r.a.createElement("div",null,r.a.createElement("div",{className:"main_feedback_body"},r.a.createElement("div",{className:"main_feedback_q"},r.a.createElement("p",null,t.q),"binary"===t.optionsType?r.a.createElement("div",{className:"all_feedback_selection"},t.options&&t.options.map(function(a,n){return r.a.createElement("div",{className:"feedback_selection",onClick:e.onPressSubmit},t.iconNames&&r.a.createElement(q.a,{name:t.iconNames[n]}),a)})):r.a.createElement("div",{className:"all_feedback_selection all_feedback_selection_col"},t.options&&t.options.map(function(t){return r.a.createElement("div",{className:"feedback_selection",onClick:e.onPressSubmit},t)}))))))}}]),t}(n.Component)),ee=(a(274),function(e){function t(){return Object(l.a)(this,t),Object(i.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(o.a)(t,[{key:"render",value:function(){return r.a.createElement(h.a,null,r.a.createElement(d.a,null,r.a.createElement(p.a,{exact:!0,path:"/",component:function(e){return r.a.createElement(y,e)}}),r.a.createElement(p.a,{exact:!0,path:"/feedback",component:function(e){return r.a.createElement(Z,e)}}),r.a.createElement(p.a,{exact:!0,path:"/place",component:function(e){return r.a.createElement(B,e)}}),r.a.createElement(p.a,{exact:!0,path:"/haggle",component:function(e){return r.a.createElement($,e)}}),r.a.createElement(p.a,{exact:!0,path:"/map",component:function(e){return r.a.createElement(K,e)}}),r.a.createElement(p.a,{component:y})))}}]),t}(n.Component));Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));s.a.render(r.a.createElement(ee,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})},32:function(e,t,a){},77:function(e,t,a){e.exports=a.p+"static/media/Price.075d9c80.svg"},78:function(e,t,a){e.exports=a.p+"static/media/Markets.ea609758.svg"},79:function(e,t,a){e.exports=a.p+"static/media/Guide.4cd99bc3.svg"},95:function(e,t,a){}},[[147,2,1]]]);
//# sourceMappingURL=main.8ee65ad1.chunk.js.map