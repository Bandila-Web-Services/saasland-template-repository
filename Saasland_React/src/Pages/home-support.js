import React from 'react';
import CustomNavbar from '../components/CustomNavbar';
import SupportBanner from '../components/Banner/SupportBanner';
import BannerData from '../components/Banner/BannerData';
import SupportPartnerlogo from '../components/SupportPartnerlogo';
import SupportItem from '../components/Service/SupportItem';
import Designtab from '../components/Features/Designtab';
import SupportIntegration from '../components/SupportIntegration';
import Price from '../components/Price';
import MarketingTestimonial from '../components/Testimonial/MarketingTestimonial';
import SupportSubscribe from '../components/SupportSubscribe';
import FooterSecurity from "../components/Footer/FooterSecurity";
import FooterData from '../components/Footer/FooterData';

const homesupport = () => {
    return(
        <div className="body_wrapper">
            CustomNavbar
            <CustomNavbar mClass="menu_four" hbtnClass="d-none"/>
            SupportBanner
            <SupportBanner/> 
            SupportPartnerlogo
            <SupportPartnerlogo BannerData={BannerData}/>
            SupportItem
            <SupportItem/>
            Designtab
            <Designtab/>
            SupportIntegration
            <SupportIntegration/>
            Price
            <Price/>
            MarketingTestimonial
            <MarketingTestimonial BannerData={BannerData}/>
            SupportSubscribe
            <SupportSubscribe/>
            FooterSecurity
            <FooterSecurity FooterData={FooterData}/>
        </div>
    )
}
export default homesupport;