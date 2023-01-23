(function(){"use strict";var e={671:function(e,t,a){var A=a(9242),n=a(3396),l=a(7718),o=a(9271);function r(e,t,a,A,r,u){const s=(0,n.up)("router-view");return(0,n.wg)(),(0,n.j4)(l.q,null,{default:(0,n.w5)((()=>[(0,n.Wm)(o.O,null,{default:(0,n.w5)((()=>[(0,n.Wm)(s)])),_:1})])),_:1})}var u={name:"App",data:()=>({})},s=a(89);const i=(0,s.Z)(u,[["render",r]]);var d=i,c=(a(9773),a(8957)),m=(0,c.Rd)();async function f(){const e=await a.e(461).then(a.t.bind(a,3657,23));e.load({google:{families:["Roboto:100,300,400,500,700,900&display=swap"]}})}var g=a(2483),w=a(7312),v=a(3369),h=a(6824);const p=e=>((0,n.dD)("data-v-52959e8a"),e=e(),(0,n.Cn)(),e),y=p((()=>(0,n._)("div",{style:{"font-size":"30px",color:"white"},class:"d-flex justify-center align-center"},"Save Paint! ",-1)));function C(e,t,a,A,o,r){return(0,n.wg)(),(0,n.j4)(l.q,{class:"hero"},{default:(0,n.w5)((()=>[(0,n.Wm)(v.K,{class:"mt-16","text-color":"white"},{default:(0,n.w5)((()=>[y,(0,n.Wm)(h.o,{class:"d-flex justify-end mt-10"},{default:(0,n.w5)((()=>[(0,n.Wm)(w.T,(0,n.dG)({variant:"text"},{icon:o.soundIcon},{color:"white",onClick:r.soundChange}),null,16,["onClick"])])),_:1}),(0,n.Wm)(h.o,{class:"d-flex justify-end"},{default:(0,n.w5)((()=>[(0,n.Wm)(w.T,{variant:"text",icon:"mdi-file-document",color:"white",onClick:t[0]||(t[0]=e=>r.movePage("/description",{page:1}))})])),_:1}),(0,n.Wm)(h.o,{class:"d-flex justify-center align-center buttons"},{default:(0,n.w5)((()=>[(0,n.Wm)(w.T,{variant:"flat",color:"red",width:"15%",onClick:t[1]||(t[1]=e=>r.movePage("/select"))},{default:(0,n.w5)((()=>[(0,n.Uk)(" Game Start ")])),_:1})])),_:1}),(0,n.Wm)(h.o,{class:"d-flex justify-center aligncenter mt-6"},{default:(0,n.w5)((()=>[(0,n.Wm)(w.T,{variant:"flat",color:"yellow",width:"15%",class:"text-white",onClick:t[2]||(t[2]=e=>r.movePage("/transform"))},{default:(0,n.w5)((()=>[(0,n.Uk)(" Paint My Image ")])),_:1})])),_:1})])),_:1})])),_:1})}a(7658);var x={data(){return{absolute:!0,overlay:!1,soundIcon:"mdi-volume-high",currentPage:"page1"}},methods:{movePage(e,t){this.$router.push({path:e,query:t})},soundChange(){"mdi-volume-high"==this.soundIcon?this.soundIcon="mdi-volume-off":this.soundIcon="mdi-volume-high"}}};const W=(0,s.Z)(x,[["render",C],["__scopeId","data-v-52959e8a"]]);var b=W,D=a(7139),q=a(6761),B=a(6572),P=a(8521),Q=a(5580);const j=e=>((0,n.dD)("data-v-25c0f53f"),e=e(),(0,n.Cn)(),e),k=j((()=>(0,n._)("div",{style:{"font-size":"30px",color:"white"},class:"d-flex justify-center align-center"},"Save Paint!",-1)));function I(e,t,a,A,o,r){return(0,n.wg)(),(0,n.j4)(l.q,{class:"hero"},{default:(0,n.w5)((()=>[(0,n.Wm)(v.K,{height:"100%"},{default:(0,n.w5)((()=>[(0,n.Wm)(h.o,{class:"d-flex justify-center mt-10"},{default:(0,n.w5)((()=>[k])),_:1}),(0,n.Wm)(h.o,{class:"mt-16"},{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"6"},{default:(0,n.w5)((()=>[(0,n.Wm)(q._,{class:"mx-auto mb-16",style:{width:"150px"}},{default:(0,n.w5)((()=>[(0,n.Wm)(B.E,{class:"text-center"},{default:(0,n.w5)((()=>[(0,n.Uk)("Mode")])),_:1})])),_:1}),(0,n.Wm)(Q.r,{modelValue:o.selectedMode,"onUpdate:modelValue":t[0]||(t[0]=e=>o.selectedMode=e)},{default:(0,n.w5)((()=>[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(o.modeItems,(e=>((0,n.wg)(),(0,n.j4)(w.T,{rounded:"",key:e.value,value:e.value,onClick:t=>r.changeMode(e.value),class:(0,D.C_)({darken:o.selectedMode===e.value,"mb-4 w-50 mx-auto grey":!0})},{default:(0,n.w5)((()=>[(0,n.Uk)((0,D.zw)(e.text),1)])),_:2},1032,["value","onClick","class"])))),128))])),_:1},8,["modelValue"])])),_:1}),(0,n.Wm)(P.D,{cols:"6"},{default:(0,n.w5)((()=>[(0,n.Wm)(q._,{class:"mx-auto mb-16",style:{width:"150px"}},{default:(0,n.w5)((()=>[(0,n.Wm)(B.E,{class:"text-center"},{default:(0,n.w5)((()=>[(0,n.Uk)("Category")])),_:1})])),_:1}),(0,n.Wm)(Q.r,{modelValue:o.selectedCategory,"onUpdate:modelValue":t[1]||(t[1]=e=>o.selectedCategory=e)},{default:(0,n.w5)((()=>[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(o.categoryItems,(e=>((0,n.wg)(),(0,n.j4)(w.T,{rounded:"",key:e.value,value:e.value,onClick:t=>r.changeCategory(e.value),class:(0,D.C_)({darken:o.selectedCategory===e.value,"mb-4 w-50 mx-auto grey":!0})},{default:(0,n.w5)((()=>[(0,n.Uk)((0,D.zw)(e.text),1)])),_:2},1032,["value","onClick","class"])))),128))])),_:1},8,["modelValue"])])),_:1})])),_:1}),(0,n.Wm)(P.D,{cols:"12",class:"d-flex justify-center mt-16"},{default:(0,n.w5)((()=>[(0,n.Wm)(w.T,{disabled:r.categoryIsEmpty,color:"primary",onClick:r.startGame},{default:(0,n.w5)((()=>[(0,n.Uk)("Game start")])),_:1},8,["disabled","onClick"])])),_:1})])),_:1})])),_:1})}var E={data(){return{categoryItems:[{text:"Animal",value:"animal"},{text:"Landmark",value:"landmark"},{text:"Entertainment",value:"entertainer"}],selectedCategory:"",selectedMode:"",modeItems:[{text:"Paint Transformer",value:"painttransformer"}]}},computed:{categoryIsEmpty(){return""===this.selectedCategory||""===this.selectedMode}},methods:{startGame(){this.$router.push({path:"/demo",query:{category:this.selectedCategory,mode:this.selectedMode}})},changeMode(e){this.selectedMode=e},changeCategory(e){this.selectedCategory=e}}};const V=(0,s.Z)(E,[["render",I],["__scopeId","data-v-25c0f53f"]]);var H=V,O=a(4870),X=a.p+"img/example.eeaf0a90.jpg",z=a(65),_=a(9029),Y=a(8694),G=a(7325),M=a(2902);const N={style:{"font-size":"30px",color:"black"},class:"d-flex justify-center align-center"};var T={__name:"GameView",setup(e){const t=(0,O.iH)(100),a=(0,O.iH)(100),o=(0,O.iH)(0),r=(0,O.iH)("Save Paint!"),u=(0,O.iH)(""),s=(0,O.iH)([]),i=(0,O.iH)([]),d=(0,O.iH)([]),c=(0,g.tv)(),m=(0,z.oR)(),f=(0,O.iH)([]),p=(0,O.iH)(0),y="A";function C(){p.value=1}setInterval((()=>{1==p.value&&(t.value=t.value-1)}),150),setInterval((()=>{1==p.value&&(a.value=a.value-1)}),1800);const x=(0,n.Fl)((function(){return o.value>0&&i.value.length>0?`data:image/gif;base64, ${i.value[o.value-1]}`:null}));function W(){o.value+=1,t.value=100,r.value=`${o.value}/9`,u.value=""}function b(){W(),a.value=100}function q(){8===o.value&&(m.commit("setRank",y),c.push({path:"/rank"})),u.value==d.value[o.value-1]?W():u.value=""}return(0,n.bv)((async()=>{const e={"Content-Type":"application/json"},t=c.currentRoute.value.query,a={category:t.category,mode:t.mode};let A=await _.Z.post("http://127.0.0.1:8000/api/v1/game/gamestart",a,{headers:e});s.value=A.data.origin_img,i.value=A.data.paint_img,d.value=A.data.answer,f.value=A.data.result_img,m.commit("setOrigin",A.data.origin_img),m.commit("setPaint",A.data.paint_img),m.commit("setAnswer",A.data.answer),m.commit("setResult",A.data.result_img)})),(0,n.YP)(t,(e=>{0==e&&W()})),(0,n.YP)(a,(e=>{0==e&&c.push({path:"/rank",props:{rank:"A"}})})),(e,s)=>((0,n.wg)(),(0,n.j4)(l.q,null,{default:(0,n.w5)((()=>[(0,n.Wm)(v.K,null,{default:(0,n.w5)((()=>[(0,n.Wm)(h.o,{class:"d-flex justify-center mt-16"},{default:(0,n.w5)((()=>[(0,n._)("div",N,(0,D.zw)(r.value),1)])),_:1}),(0,n.Wm)(h.o,{class:"d-flex mt-16"},{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"4"}),(0,n.Wm)(P.D,{cols:"4"},{default:(0,n.w5)((()=>[(0,n.wy)((0,n.Wm)(Y.f,{src:X,height:"350",width:"350",class:"mx-auto"},null,512),[[A.F8,0===o.value]]),0!=o.value?((0,n.wg)(),(0,n.j4)(Y.f,{key:0,src:(0,O.SU)(x),class:"mx-auto",height:"350",width:"350",onLoad:C},null,8,["src"])):(0,n.kq)("",!0)])),_:1}),(0,n.Wm)(P.D,{cols:"4"},{default:(0,n.w5)((()=>[(0,n.wy)((0,n.Wm)(G.K,{class:"rotate",height:"20",width:"40",modelValue:a.value,"onUpdate:modelValue":s[0]||(s[0]=e=>a.value=e)},null,8,["modelValue"]),[[A.F8,o.value>0]])])),_:1})])),_:1}),(0,n.Wm)(h.o,{class:"d-flex justify-center mt-8"},{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"4"},{default:(0,n.w5)((()=>[(0,n.wy)((0,n.Wm)(G.K,{modelValue:t.value,"onUpdate:modelValue":s[1]||(s[1]=e=>t.value=e),height:"7",rounded:"",color:"indigo"},null,8,["modelValue"]),[[A.F8,o.value>0]])])),_:1})])),_:1}),(0,n.Wm)(h.o,{class:"d-flex justify-center mt-10"},{default:(0,n.w5)((()=>[(0,n.wy)((0,n.Wm)(M.hw,{class:"text",clearable:"","hide-details":"auto",height:"10px",label:"Enter the answer","single-line":"",density:"compact",modelValue:u.value,"onUpdate:modelValue":s[2]||(s[2]=e=>u.value=e),onKeydown:(0,A.D2)(q,["enter"])},null,8,["modelValue","onKeydown"]),[[A.F8,o.value>0]]),(0,n.wy)((0,n.Wm)(w.T,{onClick:b},{default:(0,n.w5)((()=>[(0,n.Uk)("Game Start!")])),_:1},512),[[A.F8,0==o.value]])])),_:1})])),_:1})])),_:1}))}};const L=(0,s.Z)(T,[["__scopeId","data-v-1d32a7ee"]]);var J=L;function F(e,t,a,A,l,o){const r=(0,n.up)("mainview");return(0,n.wg)(),(0,n.j4)(r,{page:e.$route.query.page},null,8,["page"])}var U=a(9234),Z=a(73);const K=e=>((0,n.dD)("data-v-544d7580"),e=e(),(0,n.Cn)(),e),R=K((()=>(0,n._)("div",{style:{"font-size":"30px",color:"white"},class:"no-overlay-container"},"4/9",-1))),S=K((()=>(0,n._)("br",null,null,-1)));function $(e,t,a,l,o,r){return(0,n.wg)(),(0,n.j4)(Z.yc,{modelValue:o.overlay,"onUpdate:modelValue":t[8]||(t[8]=e=>o.overlay=e),"z-index":"500",width:"100%",height:"100%"},{default:(0,n.w5)((()=>[(0,n.Wm)(v.K,{onClick:t[7]||(t[7]=(0,A.iM)((()=>{}),["stop"])),style:{position:"relative"}},{default:(0,n.w5)((()=>[(0,n.Wm)(h.o,null,{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"12"}),(0,n.Wm)(P.D,{cols:"12"})])),_:1}),(0,n.Wm)(h.o,{class:"justify-center"},{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"4",class:"d-flex justify-center align-center text-white no-overlay-container"},{default:(0,n.w5)((()=>[(0,n.wy)((0,n._)("div",null,[(0,n.Uk)(" 1.현재 진행중인 게임 라운드와 총 라운드 수입니다. "),(0,n.Wm)(w.T,{class:"ma-2",icon:"mdi-arrow-left-bold",variant:"text",onClick:r.moveHome},null,8,["onClick"]),(0,n.Wm)(w.T,{class:"ma-2",icon:"mdi-arrow-right-bold",variant:"text",onClick:t[0]||(t[0]=e=>r.changeQuery(2))})],512),[[A.F8,1==a.page]])])),_:1}),R,(0,n.Wm)(P.D,{cols:"2"}),(0,n.Wm)(P.D,{cols:"2",class:"justify-center align-center text-white no-overlay-container"},{default:(0,n.w5)((()=>[(0,n.wy)((0,n._)("div",null,[(0,n.Uk)(" 4. 남은 물감의 양입니다. 그림을 그리면서 물감이 소모되며, 소진 시 미션 실패로 게임이 종료됩니다 "),(0,n.Wm)(w.T,{class:"ma-2",icon:"mdi-arrow-left-bold",variant:"text",onClick:t[1]||(t[1]=e=>r.changeQuery(3))}),(0,n.Wm)(w.T,{class:"ma-2",icon:"mdi-arrow-right-bold",variant:"text",onClick:r.moveHome},null,8,["onClick"])],512),[[A.F8,4==a.page]])])),_:1})])),_:1}),(0,n.Wm)(h.o,null,{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"12"})])),_:1}),(0,n.Wm)(h.o,null,{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"4",class:"d-flex justify-center align-center text-white no-overlay-container",style:{position:"relative",top:"100px"}},{default:(0,n.w5)((()=>[(0,n.wy)((0,n._)("div",null,[(0,n.Uk)(" 2. 현재 라운드에 해당하는 이미지를 생성합니다. "),(0,n.Wm)(w.T,{class:"ma-2",icon:"mdi-arrow-left-bold",variant:"text",onClick:t[2]||(t[2]=e=>r.changeQuery(1))}),(0,n.Wm)(w.T,{class:"ma-2",icon:"mdi-arrow-right-bold",variant:"text",onClick:t[3]||(t[3]=e=>r.changeQuery(3))})],512),[[A.F8,2==a.page]])])),_:1}),(0,n.Wm)(Y.f,{src:X,height:"270",width:"270",class:"no-overlay-container"}),(0,n.Wm)(P.D),(0,n.Wm)(P.D,{cols:"3",class:"rotate"},{default:(0,n.w5)((()=>[(0,n.Wm)(G.K,{height:"20",width:"40",modelValue:o.valueDeterminate,"onUpdate:modelValue":t[4]||(t[4]=e=>o.valueDeterminate=e)},null,8,["modelValue"])])),_:1})])),_:1}),(0,n.Wm)(h.o,null,{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"12"},{default:(0,n.w5)((()=>[(0,n.Wm)(U.C)])),_:1}),(0,n.Wm)(P.D,{cols:"12",class:"d-flex justify-center align-center text-white no-overlay-container"},{default:(0,n.w5)((()=>[(0,n.wy)((0,n._)("div",null,[(0,n.Uk)(" 3. 정답을 입력할 수 있는 칸입니다. "),S,(0,n.Wm)(w.T,{class:"ma-2",icon:"mdi-arrow-left-bold",variant:"text",onClick:t[5]||(t[5]=e=>r.changeQuery(2))}),(0,n.Wm)(w.T,{class:"ma-2",icon:"mdi-arrow-right-bold",variant:"text",onClick:t[6]||(t[6]=e=>r.changeQuery(4))})],512),[[A.F8,3==a.page]])])),_:1})])),_:1}),(0,n.Wm)(h.o,{class:"justify-center"},{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"4"},{default:(0,n.w5)((()=>[(0,n.Wm)(M.hw,{clearable:"","hide-details":"auto",label:"Answer"})])),_:1})])),_:1})])),_:1})])),_:1},8,["modelValue"])}var ee={props:["page"],data(){return{valueDeterminate:50,overlay:!0}},methods:{changeQuery(e){this.$router.replace({query:{page:e}})},moveHome(){this.$router.push({path:"/"})}}};const te=(0,s.Z)(ee,[["render",$],["__scopeId","data-v-544d7580"]]);var ae=te,Ae={components:{mainview:ae},data(){return{overlay:!0}}};const ne=(0,s.Z)(Ae,[["render",F],["__scopeId","data-v-62b74dea"]]);var le=ne;const oe=e=>((0,n.dD)("data-v-406209d9"),e=e(),(0,n.Cn)(),e),re=oe((()=>(0,n._)("div",{style:{"font-size":"30px",color:"black"},class:"mx-auto"},"Result",-1)));function ue(e,t,a,A,o,r){return(0,n.wg)(),(0,n.j4)(l.q,null,{default:(0,n.w5)((()=>[(0,n.Wm)(v.K,null,{default:(0,n.w5)((()=>[(0,n.Wm)(h.o,{class:"d-flex child -flex mt-10 mb-10"},{default:(0,n.w5)((()=>[re])),_:1}),""!=o.originImg?((0,n.wg)(),(0,n.j4)(h.o,{key:0},{default:(0,n.w5)((()=>[((0,n.wg)(),(0,n.iD)(n.HY,null,(0,n.Ko)(9,(e=>(0,n.Wm)(P.D,{key:e,class:"d-flex child-flex no-padding",cols:"4"},{default:(0,n.w5)((()=>[(0,n.Wm)(Y.f,{width:350,height:350,src:`data:image/gif;base64,${o.result[e-1]}`,"lazy-src":"https://picsum.photos/10/6?image="+(5*e+10),"aspect-ratio":"1",cover:"",class:"grey lighten-2",onClick:t=>r.moveDetail(e)},null,8,["src","lazy-src","onClick"])])),_:2},1024))),64))])),_:1})):(0,n.kq)("",!0)])),_:1})])),_:1})}var se={data(){return{originImg:this.$store.state.originImg,paintImg:this.$store.state.paintImg,answer:this.$store.state.answer,result:this.$store.state.result}},methods:{moveDetail(e){this.$router.push({path:"/detail",query:{index:e}})}}};const ie=(0,s.Z)(se,[["render",ue],["__scopeId","data-v-406209d9"]]);var de=ie;const ce={style:{"font-size":"30px",color:"black"},class:"mx-auto"};function me(e,t,a,A,o,r){return(0,n.wg)(),(0,n.j4)(l.q,null,{default:(0,n.w5)((()=>[(0,n.Wm)(v.K,null,{default:(0,n.w5)((()=>[(0,n.Wm)(h.o,{class:"d-flex child -flex mt-12 mb-12"},{default:(0,n.w5)((()=>[(0,n._)("div",ce,(0,D.zw)(o.answer[o.index-1]),1)])),_:1}),(0,n.Wm)(h.o,null,{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"6"},{default:(0,n.w5)((()=>[(0,n.Wm)(Y.f,{src:`data:image/gif;base64,${o.originImg[o.index-1]}`},null,8,["src"])])),_:1}),(0,n.Wm)(P.D,{cols:"6"},{default:(0,n.w5)((()=>[(0,n.Wm)(Y.f,{src:`data:image/gif;base64,${o.paintImg[o.index-1]}`},null,8,["src"])])),_:1})])),_:1})])),_:1})])),_:1})}var fe={data(){return{index:this.$route.query.index,originImg:this.$store.state.originImg,paintImg:this.$store.state.paintImg,answer:this.$store.state.answer}}};const ge=(0,s.Z)(fe,[["render",me]]);var we=ge,ve=a(8258),he=a(3173);function pe(e,t,a,o,r,u){return(0,n.wg)(),(0,n.j4)(l.q,{class:"hero"},{default:(0,n.w5)((()=>[(0,n.Wm)(v.K,null,{default:(0,n.w5)((()=>[(0,n.Wm)(h.o,{class:"mt-16"},{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"8",class:"mx-auto"},{default:(0,n.w5)((()=>[(0,n.Wm)(ve.Z,{clearable:"",label:"File input",variant:"solo",onChange:u.setImg},null,8,["onChange"])])),_:1}),(0,n.Wm)(P.D,{cols:"2",class:"align-center mt-2"},{default:(0,n.w5)((()=>[(0,n.Wm)(w.T,{onClick:u.transformImg,disabled:null==r.image},{default:(0,n.w5)((()=>[(0,n.Uk)("Transform!")])),_:1},8,["onClick","disabled"])])),_:1})])),_:1}),(0,n.Wm)(h.o,{class:"mt-16"},{default:(0,n.w5)((()=>[(0,n.Wm)(Y.f,{"max-height":"400",class:"mx-auto","max-width":"400",src:`data:image/gif;base64,${r.returnImg}`},{default:(0,n.w5)((()=>[(0,n.wy)((0,n.Wm)(he.L,{class:"loading",color:"grey-lighten-4",indeterminate:""},null,512),[[A.F8,1==r.transform]])])),_:1},8,["src"])])),_:1})])),_:1})])),_:1})}var ye={data(){return{image:null,transform:!1,returnImg:null,img_loaded:!1}},computed:{},methods:{setImg(e){this.image=e.target.files[0]},async transformImg(){this.transform=!0;const e=new FormData;e.append("file",this.image);let t=await this.$api2("http://127.0.0.1:8000/api/v1/infer","POST",e);this.returnImg=t["image"],this.transform=!1}}};const Ce=(0,s.Z)(ye,[["render",pe]]);var xe=Ce;const We=e=>((0,n.dD)("data-v-76aa027c"),e=e(),(0,n.Cn)(),e),be=We((()=>(0,n._)("div",{style:{"font-size":"30px",color:"black"},class:"d-flex justify-center align-center"}," Score",-1)));function De(e,t,a,o,r,u){const s=(0,n.up)("F"),i=(0,n.up)("S");return(0,n.wg)(),(0,n.j4)(l.q,{class:"hero"},{default:(0,n.w5)((()=>[(0,n.Wm)(v.K,null,{default:(0,n.w5)((()=>[(0,n.Wm)(h.o,{class:"d-flex justify-center mt-16"},{default:(0,n.w5)((()=>[be])),_:1}),(0,n.Wm)(h.o,null,{default:(0,n.w5)((()=>[(0,n.wy)((0,n.Wm)(s,{height:"300",class:"score-space mx-auto"},null,512),[[A.F8,"F"==r.rank]]),(0,n.wy)((0,n.Wm)(i,{height:"300",class:"score-space mx-auto"},null,512),[[A.F8,"S"==r.rank]])])),_:1}),(0,n.Wm)(h.o,null,{default:(0,n.w5)((()=>[(0,n.Wm)(w.T,{class:"mx-auto mt-16",onClick:u.goResult},{default:(0,n.w5)((()=>[(0,n.Uk)(" Show Result! ")])),_:1},8,["onClick"])])),_:1})])),_:1})])),_:1})}const qe={viewBox:"0 0 320 512",xmlns:"http://www.w3.org/2000/svg"},Be=(0,n._)("path",{d:"M320 64.01c0 17.67-14.33 32-32 32H64v128h160c17.67 0 32 14.32 32 31.1s-14.33 32-32 32H64v160c0 17.67-14.33 32-32 32s-32-14.33-32-32v-384C0 46.34 14.33 32.01 32 32.01h256C305.7 32.01 320 46.34 320 64.01z"},null,-1),Pe=[Be];function Qe(e,t){return(0,n.wg)(),(0,n.iD)("svg",qe,Pe)}const je={},ke=(0,s.Z)(je,[["render",Qe]]);var Ie=ke;const Ee={viewBox:"0 0 384 512",xmlns:"http://www.w3.org/2000/svg"},Ve=(0,n._)("path",{d:"M155.3 154.6c0-22.3 18.6-30.9 48.4-30.9 43.4 0 98.5 13.3 141.9 36.7V26.1C298.3 7.2 251.1 0 203.8 0 88.1 0 11 60.4 11 161.4c0 157.9 216.8 132.3 216.8 200.4 0 26.4-22.9 34.9-54.7 34.9-47.2 0-108.2-19.5-156.1-45.5v128.5a396.09 396.09 0 0 0 156 32.4c118.6 0 200.3-51 200.3-153.6 0-170.2-218-139.7-218-203.9z"},null,-1),He=[Ve];function Oe(e,t){return(0,n.wg)(),(0,n.iD)("svg",Ee,He)}const Xe={},ze=(0,s.Z)(Xe,[["render",Oe]]);var _e=ze,Ye={components:{F:Ie,S:_e},data(){return{rank:"S"}},methods:{goResult(){this.$router.push({path:"/demoresult"})}}};const Ge=(0,s.Z)(Ye,[["render",De],["__scopeId","data-v-76aa027c"]]);var Me=Ge;const Ne={style:{"font-size":"30px",color:"black"},class:"d-flex justify-center align-center"};var Te={__name:"DemoView",setup(e){const t=(0,O.iH)(100),a=(0,O.iH)(100),o=(0,O.iH)(0),r=(0,O.iH)("Save Paint!"),u=(0,O.iH)(""),s=(0,O.iH)(""),i=(0,O.iH)(""),d=(0,O.iH)([]),c=(0,g.tv)(),m=(0,z.oR)(),f=(0,O.iH)(0),p="A",y=(0,O.iH)([]);function C(){f.value=1}setInterval((()=>{1==f.value&&(t.value=t.value-1)}),150),setInterval((()=>{1==f.value&&(a.value=a.value-1)}),1800);const x=async()=>{if(o.value>8)return;const e=await _.Z.post("http://127.0.0.1:8000/api/v1/game/paint",{path:y.value[o.value]},{responseType:"arraybuffer"}),t=new Uint8Array(e.data);let a=t.length,A=new Array,n=0;for(let o=0;o<a;o+=1024)A.push(t.slice(n,n+1024)),n+=1024;const l=new Blob(A,{type:"image/gif"});i.value=URL.createObjectURL(l)};function W(){o.value+=1,t.value=100,r.value=`${o.value}/9`,u.value="",s.value=i.value,x()}function b(){W(),a.value=100}function q(){9===o.value&&(m.commit("setRank",p),c.push({path:"/rank"})),u.value==d.value[o.value-1]?W():u.value=""}return(0,n.bv)((async()=>{const e=c.currentRoute.value.query,t={category:e.category,mode:e.mode},a={"Content-Type":"application/json"},A=await _.Z.post("http://127.0.0.1:8000/api/v1/game/gamestart",t,a);y.value=A.data.img_list,d.value=A.data.answer_list,m.commit("setPath",A.data.img_list),console.log(d.value);const n=await _.Z.post("http://127.0.0.1:8000/api/v1/game/paint",{path:y.value[0]},{headers:{"Content-Type":"application/json"},responseType:"arraybuffer"}),l=new Uint8Array(n.data);let o=l.length,r=new Array,u=0;for(let i=0;i<o;i+=1024)r.push(l.slice(u,u+1024)),u+=1024;const s=new Blob(r,{type:"image/gif"});i.value=URL.createObjectURL(s)})),(0,n.YP)(t,(e=>{0==e&&W()})),(0,n.YP)(a,(e=>{0==e&&c.push({path:"/rank",props:{rank:"A"}})})),(e,d)=>((0,n.wg)(),(0,n.j4)(l.q,null,{default:(0,n.w5)((()=>[(0,n.Wm)(v.K,null,{default:(0,n.w5)((()=>[(0,n.Wm)(h.o,{class:"d-flex justify-center mt-16"},{default:(0,n.w5)((()=>[(0,n._)("div",Ne,(0,D.zw)(r.value),1)])),_:1}),(0,n.Wm)(h.o,{class:"d-flex mt-16"},{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"4"}),(0,n.Wm)(P.D,{cols:"4"},{default:(0,n.w5)((()=>[(0,n.wy)((0,n.Wm)(Y.f,{src:X,height:"350",width:"350",class:"mx-auto"},null,512),[[A.F8,0===o.value]]),(0,n.wy)((0,n.Wm)(Y.f,{src:s.value,class:"mx-auto",height:"350",width:"350",onLoad:C},null,8,["src"]),[[A.F8,0!=o.value]])])),_:1}),(0,n.Wm)(P.D,{cols:"4"},{default:(0,n.w5)((()=>[(0,n.wy)((0,n.Wm)(G.K,{class:"rotate",height:"20",width:"40",modelValue:a.value,"onUpdate:modelValue":d[0]||(d[0]=e=>a.value=e)},null,8,["modelValue"]),[[A.F8,o.value>0]])])),_:1})])),_:1}),(0,n.Wm)(h.o,{class:"d-flex justify-center mt-8"},{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"4"},{default:(0,n.w5)((()=>[(0,n.wy)((0,n.Wm)(G.K,{modelValue:t.value,"onUpdate:modelValue":d[1]||(d[1]=e=>t.value=e),height:"7",rounded:"",color:"indigo"},null,8,["modelValue"]),[[A.F8,o.value>0]])])),_:1})])),_:1}),(0,n.Wm)(h.o,{class:"d-flex justify-center mt-10"},{default:(0,n.w5)((()=>[(0,n.wy)((0,n.Wm)(M.hw,{class:"text",clearable:"","hide-details":"auto",height:"10px",label:"Enter the answer","single-line":"",density:"compact",modelValue:u.value,"onUpdate:modelValue":d[2]||(d[2]=e=>u.value=e),onKeydown:(0,A.D2)(q,["enter"])},null,8,["modelValue","onKeydown"]),[[A.F8,o.value>0]]),(0,n.wy)((0,n.Wm)(w.T,{onClick:b},{default:(0,n.w5)((()=>[(0,n.Uk)("Game Start!")])),_:1},512),[[A.F8,0==o.value&&""!=i.value]])])),_:1})])),_:1})])),_:1}))}};const Le=(0,s.Z)(Te,[["__scopeId","data-v-06a1a320"]]);var Je=Le;const Fe=e=>((0,n.dD)("data-v-bc7d53d0"),e=e(),(0,n.Cn)(),e),Ue=Fe((()=>(0,n._)("div",{style:{"font-size":"30px",color:"black"},class:"mx-auto"},"Result",-1)));function Ze(e,t,a,A,o,r){return(0,n.wg)(),(0,n.j4)(l.q,null,{default:(0,n.w5)((()=>[(0,n.Wm)(v.K,null,{default:(0,n.w5)((()=>[(0,n.Wm)(h.o,{class:"d-flex child -flex mt-10 mb-10"},{default:(0,n.w5)((()=>[Ue])),_:1}),(0,n.Wm)(h.o,null,{default:(0,n.w5)((()=>[((0,n.wg)(),(0,n.iD)(n.HY,null,(0,n.Ko)(9,(e=>(0,n.Wm)(P.D,{key:e,class:"d-flex child-flex no-padding",cols:"4"},{default:(0,n.w5)((()=>[(0,n.Wm)(Y.f,{width:350,height:350,"lazy-src":"https://picsum.photos/10/6?image="+(5*e+10),"aspect-ratio":"1",cover:"",src:`data:image/gif;base64,${o.originImg[e-1]}`,class:"grey lighten-2",onClick:t=>r.moveDetail(e)},null,8,["lazy-src","src","onClick"])])),_:2},1024))),64))])),_:1})])),_:1})])),_:1})}var Ke={data(){return{originImg:"",imgList:this.$store.state.imgList}},methods:{moveDetail(e){this.$router.push({path:"/demodetail",query:{index:e}})}},async mounted(){let e=await _.Z.post("http://127.0.0.1:8000/api/v1/game/result",{paths:this.imgList},{"Content-Type":"application/json"});this.originImg=e.data.origin_imgs,this.$store.commit("setOrigin",e.data.origin_imgs),this.$store.commit("setResult",e.data.result_imgs)}};const Re=(0,s.Z)(Ke,[["render",Ze],["__scopeId","data-v-bc7d53d0"]]);var Se=Re;function $e(e,t,a,A,o,r){return(0,n.wg)(),(0,n.j4)(l.q,null,{default:(0,n.w5)((()=>[(0,n.Wm)(v.K,null,{default:(0,n.w5)((()=>[(0,n.Wm)(h.o,{class:"d-flex child -flex mt-12 mb-12"}),(0,n.Wm)(h.o,null,{default:(0,n.w5)((()=>[(0,n.Wm)(P.D,{cols:"6"},{default:(0,n.w5)((()=>[(0,n.Wm)(Y.f,{src:`data:image/gif;base64,${o.originImg[o.index-1]}`},null,8,["src"])])),_:1}),(0,n.Wm)(P.D,{cols:"6"},{default:(0,n.w5)((()=>[(0,n.Wm)(Y.f,{src:`data:image/gif;base64,${o.paintImg[o.index-1]}`},null,8,["src"])])),_:1})])),_:1})])),_:1})])),_:1})}var et={data(){return{index:this.$route.query.index,originImg:this.$store.state.originImg,paintImg:this.$store.state.result}}};const tt=(0,s.Z)(et,[["render",$e]]);var at=tt;const At=[{path:"/",name:"start",component:b},{path:"/select",name:"select",component:H},{path:"/game",name:"game",component:J},{path:"/description",name:"description",component:le},{path:"/result",name:"result",component:de},{path:"/detail",name:"detail",component:we},{path:"/transform",name:"transform",component:xe},{path:"/rank",name:"rank",component:Me},{path:"/demo",name:"demo",component:Je},{path:"/demoresult",name:"demoresult",component:Se},{path:"/demodetail",name:"demodetail",component:at}],nt=(0,g.p7)({history:(0,g.PO)("/"),routes:At});var lt=nt,ot={methods:{async $api2(e,t,a){return(await(0,_.Z)({method:t,url:e,headers:{"Content-Type":"multipart/form-data"},data:a}).catch((e=>{console.log(e)}))).data}}};const rt=(0,n.aZ)({template:'<svg width="240" height="233" viewBox="0 0 240 233" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n  <rect width="240" height="233" fill="url(#pattern0)"/>\n  <defs>\n  <pattern id="pattern0" patternContentUnits="objectBoundingBox" width="1" height="1">\n  <use xlink:href="#image0_259_476" transform="translate(0 -0.0150215) scale(0.00195312 0.0020118)"/>\n  </pattern>\n  <image id="image0_259_476" width="512" height="512" xlink:href="data:image/png;base64,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"/>\n  </defs>\n  </svg>'});var ut=rt,st=a(2415);const it=(0,z.MT)({state(){return{originImg:[],paintImg:[],answer:[],result:[],rank:"S",imgList:[]}},mutations:{setOrigin(e,t){e.originImg=t},setPaint(e,t){e.paintImg=t},setAnswer(e,t){e.answer=t},setResult(e,t){e.result=t},setRank(e,t){e.rank=t},setPath(e,t){e.imgList=t}},plugins:[(0,st.Z)()]});var dt=it;f();const ct=(0,A.ri)(d);ct.use(lt),ct.use(dt),ct.use(m,{icons:{"my-icon":ut}}),ct.mixin(ot),ct.mount("#app")}},t={};function a(A){var n=t[A];if(void 0!==n)return n.exports;var l=t[A]={exports:{}};return e[A](l,l.exports,a),l.exports}a.m=e,function(){var e=[];a.O=function(t,A,n,l){if(!A){var o=1/0;for(i=0;i<e.length;i++){A=e[i][0],n=e[i][1],l=e[i][2];for(var r=!0,u=0;u<A.length;u++)(!1&l||o>=l)&&Object.keys(a.O).every((function(e){return a.O[e](A[u])}))?A.splice(u--,1):(r=!1,l<o&&(o=l));if(r){e.splice(i--,1);var s=n();void 0!==s&&(t=s)}}return t}l=l||0;for(var i=e.length;i>0&&e[i-1][2]>l;i--)e[i]=e[i-1];e[i]=[A,n,l]}}(),function(){a.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return a.d(t,{a:t}),t}}(),function(){var e,t=Object.getPrototypeOf?function(e){return Object.getPrototypeOf(e)}:function(e){return e.__proto__};a.t=function(A,n){if(1&n&&(A=this(A)),8&n)return A;if("object"===typeof A&&A){if(4&n&&A.__esModule)return A;if(16&n&&"function"===typeof A.then)return A}var l=Object.create(null);a.r(l);var o={};e=e||[null,t({}),t([]),t(t)];for(var r=2&n&&A;"object"==typeof r&&!~e.indexOf(r);r=t(r))Object.getOwnPropertyNames(r).forEach((function(e){o[e]=function(){return A[e]}}));return o["default"]=function(){return A},a.d(l,o),l}}(),function(){a.d=function(e,t){for(var A in t)a.o(t,A)&&!a.o(e,A)&&Object.defineProperty(e,A,{enumerable:!0,get:t[A]})}}(),function(){a.f={},a.e=function(e){return Promise.all(Object.keys(a.f).reduce((function(t,A){return a.f[A](e,t),t}),[]))}}(),function(){a.u=function(e){return"js/webfontloader.fb07477b.js"}}(),function(){a.miniCssF=function(e){}}(),function(){a.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){a.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={},t="vue-project:";a.l=function(A,n,l,o){if(e[A])e[A].push(n);else{var r,u;if(void 0!==l)for(var s=document.getElementsByTagName("script"),i=0;i<s.length;i++){var d=s[i];if(d.getAttribute("src")==A||d.getAttribute("data-webpack")==t+l){r=d;break}}r||(u=!0,r=document.createElement("script"),r.charset="utf-8",r.timeout=120,a.nc&&r.setAttribute("nonce",a.nc),r.setAttribute("data-webpack",t+l),r.src=A),e[A]=[n];var c=function(t,a){r.onerror=r.onload=null,clearTimeout(m);var n=e[A];if(delete e[A],r.parentNode&&r.parentNode.removeChild(r),n&&n.forEach((function(e){return e(a)})),t)return t(a)},m=setTimeout(c.bind(null,void 0,{type:"timeout",target:r}),12e4);r.onerror=c.bind(null,r.onerror),r.onload=c.bind(null,r.onload),u&&document.head.appendChild(r)}}}(),function(){a.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){a.p="/"}(),function(){var e={143:0};a.f.j=function(t,A){var n=a.o(e,t)?e[t]:void 0;if(0!==n)if(n)A.push(n[2]);else{var l=new Promise((function(a,A){n=e[t]=[a,A]}));A.push(n[2]=l);var o=a.p+a.u(t),r=new Error,u=function(A){if(a.o(e,t)&&(n=e[t],0!==n&&(e[t]=void 0),n)){var l=A&&("load"===A.type?"missing":A.type),o=A&&A.target&&A.target.src;r.message="Loading chunk "+t+" failed.\n("+l+": "+o+")",r.name="ChunkLoadError",r.type=l,r.request=o,n[1](r)}};a.l(o,u,"chunk-"+t,t)}},a.O.j=function(t){return 0===e[t]};var t=function(t,A){var n,l,o=A[0],r=A[1],u=A[2],s=0;if(o.some((function(t){return 0!==e[t]}))){for(n in r)a.o(r,n)&&(a.m[n]=r[n]);if(u)var i=u(a)}for(t&&t(A);s<o.length;s++)l=o[s],a.o(e,l)&&e[l]&&e[l][0](),e[l]=0;return a.O(i)},A=self["webpackChunkvue_project"]=self["webpackChunkvue_project"]||[];A.forEach(t.bind(null,0)),A.push=t.bind(null,A.push.bind(A))}();var A=a.O(void 0,[998],(function(){return a(671)}));A=a.O(A)})();
//# sourceMappingURL=app.e48f4242.js.map