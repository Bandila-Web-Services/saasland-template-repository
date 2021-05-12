import React from 'react';
import CustomNavbar from '../components/CustomNavbar';
import PaymentBanner from '../components/Banner/PaymentBanner';
import PaymentFeatures from '../components/Features/PaymentFeatures';
import PaymentService from '../components/Service/PaymentService';
import ServiceData from '../components/Service/ServiceData';
import Paymentprocess from '../components/Paymentprocess';
import PaymentTestimonial from '../components/Testimonial/PaymentTestimonial';
import FooterThree from '../components/Footer/FooterThree';
import FooterData from '../components/Footer/FooterData';

const Paymentprocessing = () => {
    return(
        <div className="body_wrapper">
            CustomNavbar
            <CustomNavbar slogo="sticky_logo" mClass="menu_four" nClass="w_menu"/>
            PaymentBanner
            <PaymentBanner/>
            PaymentFeatures
            <PaymentFeatures/>
            PaymentService
            <PaymentService ServiceData={ServiceData}/>
            Paymentprocess
            <Paymentprocess/>
            PaymentTestimonial
            <PaymentTestimonial/>
            FooterThree
            <FooterThree FooterData={FooterData}/>
        </div>
    )
}
export default Paymentprocessing;