import React from 'react';
import CustomNavbar from '../components/CustomNavbar';
import CrmBanner from '../components/Banner/CrmBanner';
import StartupFeatures from '../components/Features/StartupFeatures';
import Stservice from '../components/Service/Sservice/StartupService';
import Testimonial from '../components/Testimonial/Testimonial';
import Cprogress from '../components/CircleProgressbar';
import PrototypeFooter from '../components/Footer/PrototypeFooter';
import FooterData from '../components/Footer/FooterData';

const HomeCRM = () => {
    return(
        <div className="body_wrapper">
            CustomNavbar
            <CustomNavbar slogo="sticky_logo" mClass="menu_four" nClass="w_menu" hbtnClass="btn_get_radious menu_custfive"/>
            CrmBanner
            <CrmBanner/>
            StartupFeatures
            <StartupFeatures/>
            Stservice
            <Stservice/>
            Cprogress
            <Cprogress/>
            Testimonial
            <Testimonial tClass="testimonial_area_four sec_pad" FooterData={FooterData}/>
            PrototypeFooter
            <PrototypeFooter rclass={'payment_footer_area_two'} FooterData={FooterData}/>
        </div>
    )
}
export default HomeCRM;