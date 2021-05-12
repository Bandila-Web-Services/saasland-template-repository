import React from 'react';
import CustomNavbar from '../components/CustomNavbar';
import Breadcrumb from '../components/Breadcrumb';
import SequrityPrice from '../components/Features/SecurityPrice';
import FooterTwo from '../components/Footer/FooterTwo';
import FooterData from '../components/Footer/FooterData';

const Price = () => {
    return(
        <div className="body_wrapper">
            CustomNavbar
            <CustomNavbar slogo="sticky_logo" mClass="menu_four" nClass="w_menu ml-auto mr-auto"/>
            Breadcrumb
            <Breadcrumb breadcrumbClass="breadcrumb_area" imgName="breadcrumb/banner_bg.png" Ptitle="Pricing Plan" Pdescription="Why I say old chap that is spiffing off his nut arse pear shaped plastered Jeffrey bodge barney some dodgy.!!"/>
            SequrityPrice
            <SequrityPrice/>
            FooterTwo
            <FooterTwo FooterData={FooterData}/>
        </div>
    )
}
export default Price;