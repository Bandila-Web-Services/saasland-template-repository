import React from 'react';
import CustomNavbar from '../components/CustomNavbar';
import AgencyBanner from '../components/Banner/AgencyBanner';
import BannerData from '../components/Banner/BannerData';
import MarketingService from '../components/Service/MarketingService';
import ServiceData from '../components/Service/ServiceData';
import AgencyAbout from '../components/About/AgencyAbout';
import Features from '../components/Features/Features';
import MarketingTestimonial from '../components/Testimonial/MarketingTestimonial';
import AgencyAction from '../components/AgencyAction';
import FooterTwo from '../components/Footer/FooterTwo';
import FooterData from '../components/Footer/FooterData';


const DigitalMarketing = () => {
    return(
        <div className="body_wrapper">
            CustomNavbar
            <CustomNavbar mClass="menu_four" cClass="custom_container p0" nClass="pl_120 mr-auto ml-auto" hbtnClass="menu_cus"/>
            AgencyBanner
            <AgencyBanner BannerData={BannerData}/>
            MarketingService
            <MarketingService ServiceData={ServiceData}/>
            AgencyAbout
            <AgencyAbout ServiceData={ServiceData}/>
            Features
            <Features/>
            MarketingTestimonial
            <MarketingTestimonial BannerData={BannerData}/>
            AgencyAction
            <AgencyAction/>
            FooterTwo
            <FooterTwo FooterData={FooterData}/>
        </div>
    )
}
export default DigitalMarketing;