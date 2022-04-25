from PIL import Image
import streamlit as st
import pandas as pd

##### Streamlit.io default page configuration #####
st.set_page_config(
page_title='Office 365 Licensing Tool',
layout="wide",
initial_sidebar_state="expanded",)
flaccid_logo = Image.open('fclogo.png')
st.image(flaccid_logo, width=450, caption='Focusing on Hardening your Office 365 Environment')



##### Global Variables #####
def defineVariables():
    global col1, col2, col3
    col1, col2, col3 = st.columns(3)
    global m365_standard_bundles
    m365_standard_bundles = st.sidebar.selectbox('Base License', ["None", "Microsoft 365 Business Apps", "Microsoft 365 Business Basic", "Microsoft 365 Business Standard", "Microsoft 365 Business Premium", "Microsoft 365 Enterprise Apps", "Microsoft 365 Enterprise F1", "Microsoft 365 Enterprise F3", "Microsoft 365 Enterprise E3", "Microsoft 365 Enterprise E3 + (E5 Sec)", "Microsoft 365 Enterprise E3 + (E5 Comp)", "Microsoft 365 Enterprise E5", "Office 365 Exchange Online Plan 1", "Office 365 Exchange Online Plan 2", "Office 365 Enterprise F3", "Office 365 Enterprise E1", "Office 365 Enterprise E3", "Office 365 Enterprise E5"])
    global m365_ems_bundles
    m365_ems_bundles = st.sidebar.selectbox('EMS Bundle', ["None", "Enterprise Mobility + Security E3", "Enterprise Mobility + Security E5"])
    global m365_mdo_bundles 
    m365_mdo_bundles = st.sidebar.selectbox('MDO Bundle', ["None", "Defender for Office P1", "Defender for Office P2"])
    global m365_w10_bundles
    m365_w10_bundles = st.sidebar.selectbox('W10 Bundle', ["None", "Windows 10 Pro", "Windows 10 E3", "Windows 10 E5"])
    global m365_aad_bundles
    m365_aad_bundles = st.sidebar.selectbox('Azure AD Bundle', ["None", "Azure Active Directory Premium P1", "Azure Active Directory Premium P2", "Free Features", "Office 365 App Plan Features"])
    global m365_base_services
    m365_base_services = pd.read_csv('base.csv', header=None).set_index(0).to_dict()
    global m365_ems_services
    m365_ems_services = pd.read_csv('ems.csv', header=None).set_index(0).to_dict()
    global m365_mdo_services
    m365_mdo_services = pd.read_csv('mdo.csv', header=None).set_index(0).to_dict()
    global m365_voip_services
    m365_voip_services = pd.read_csv('voip.csv', header=None).set_index(0).to_dict()
    global m365_w10_services
    m365_w10_services = pd.read_csv('w10.csv', header=None).set_index(0).to_dict()
    global m365_addon_services
    m365_addon_services = pd.read_csv('addon.csv', header=None).set_index(0).to_dict()
    global m365_aad_services
    m365_aad_services = pd.read_csv('aad.csv', header=None).set_index(0).to_dict()
    ##### Money Stuff #####
    global m365_pricing_import 
    m365_pricing_import = pd.read_csv('pricing.csv').squeeze().to_dict() 
    global total_cost_per_user
    total_cost_per_user = 0.0
    
    
    security_weight_ranking = {0:["Microsoft 365 Business Apps", "Microsoft 365 Business Basic", "Microsoft 365 Business Standard", "Office 365 Exchange Online Plan 1", "Office 365 Exchange Online Plan 2"], 1:["Office 365 Enterprise F3", "Office 365 Enterprise E1", "Office 365 Enterprise E3", "Office 365 Enterprise E5", "Enterprise Mobility + Security E3", "Defender for Office P1"], 2:["Microsoft 365 Business Premium", "Microsoft 365 Enterprise Apps", "Microsoft 365 Enterprise F1", "Microsoft 365 Enterprise F3", "Microsoft 365 Enterprise E3", "Microsoft 365 Enterprise E3 + (E5 Comp)", "Defender for Office P2", "Enterprise Mobility + Security E5"], 5:["Microsoft 365 Enterprise E3 + (E5 Sec)", "Microsoft 365 Enterprise E5"]}

    security_weight_ranking_items = security_weight_ranking.items()
    security_weight_total = 0
    for points, lic in security_weight_ranking_items:
        if m365_standard_bundles in lic:
            security_weight_total += points
        if m365_ems_bundles in lic:
            security_weight_total += points
        if m365_mdo_bundles in lic:
            security_weight_total += points    

    if security_weight_total == 1:
        col2.write("🍆")
        col2.caption("That is one of the smallest Security Eggplants we have ever seen...")
    elif security_weight_total == 2:
        col2.subheader("🍆")
        col2.caption("That is one average size Security Eggplant...")
    elif security_weight_total == 3:
        col2.header("🍆")
        col2.caption("Wow that is a very large Security Eggplant!!!")
    elif security_weight_total == 4:
        col2.header("🍆")
        col2.caption("Wow that is a very large Security Eggplant!!!")
    elif security_weight_total >= 5:
        col2.title("🍆")
        col2.caption("THAT IS THE BIGGEST SECURITY EGGPLANT WE HAVE EVER SEEN!!!!!")
    





##### Function to create a Security Eggplant Size Ranking System #####
# def security_eggplant_sizing_scale():
#     security_weight_ranking = {0:["Microsoft 365 Business Apps", "Microsoft 365 Business Basic", "Microsoft 365 Business Standard", "Office 365 Exchange Online Plan 1", "Office 365 Exchange Online Plan 2"], 1:["Office 365 Enterprise F3", "Office 365 Enterprise E1", "Office 365 Enterprise E3", "Office 365 Enterprise E5", "Enterprise Mobility + Security E3", "Defender for Office P1"], 2:["Microsoft 365 Business Premium", "Microsoft 365 Enterprise Apps", "Microsoft 365 Enterprise F1", "Microsoft 365 Enterprise F3", "Microsoft 365 Enterprise E3", "Microsoft 365 Enterprise E3 + (E5 Comp)", "Defender for Office P2", "Enterprise Mobility + Security E5"], 5:["Microsoft 365 Enterprise E3 + (E5 Sec)", "Microsoft 365 Enterprise E5"]}
#     security_weight_ranking_items = security_weight_ranking.items()

#     with st.sidebar.form("How big is your Security Eggplant?"):
#         base_dropdown = st.selectbox('Base License', ["None", "Microsoft 365 Business Apps", "Microsoft 365 Business Basic", "Microsoft 365 Business Standard", "Microsoft 365 Business Premium", "Microsoft 365 Enterprise Apps", "Microsoft 365 Enterprise F1", "Microsoft 365 Enterprise F3", "Microsoft 365 Enterprise E3", "Microsoft 365 Enterprise E3 + (E5 Sec)", "Microsoft 365 Enterprise E3 + (E5 Comp)", "Microsoft 365 Enterprise E5", "Office 365 Exchange Online Plan 1", "Office 365 Exchange Online Plan 2", "Office 365 Enterprise F3", "Office 365 Enterprise E1", "Office 365 Enterprise E3", "Office 365 Enterprise E5"])
#         ems_dropdown = st.selectbox('EMS Bundle', ["None", "Enterprise Mobility + Security E3", "Enterprise Mobility + Security E5"]) 
#         mdo_dropdown = st.selectbox('MDO Bundle', ["None", "Defender for Office P1", "Defender for Office P2"])
#         submitted = st.form_submit_button("Submit")

#         if submitted:
#             security_weight_total = 0
#             selection_list = []
#             selection_list.append(base_dropdown)
#             selection_list.append(ems_dropdown)
#             selection_list.append(mdo_dropdown)
            
#             for points, lic in security_weight_ranking_items:
#                 if base_dropdown in lic:
#                     security_weight_total += points
#                 if ems_dropdown in lic:
#                     security_weight_total += points
#                 if mdo_dropdown in lic:
#                     security_weight_total += points
                
#             if security_weight_total <= 1:
#                 st.write("🍆")
#                 st.caption("That is one of the smallest Security Eggplants we have ever seen...")
#             elif security_weight_total <= 2:
#                 st.subheader("🍆")
#                 st.caption("That is one average size Security Eggplant...")
#             elif security_weight_total <= 4:
#                 st.header("🍆")
#                 st.caption("Wow that is a very large Security Eggplant!!!")
#             elif security_weight_total >= 5:
#                 st.title("🍆")
#                 st.caption("THAT IS THE BIGGEST SECURITY EGGPLANT WE HAVE EVER SEEN!!!!!")

  
##### Function for the Base License Dropdown #####
def featuresProvidedBasedOnChosenBaseBundle():
    for m365_base_service in m365_base_services:
        for feature, license in m365_base_services[m365_base_service].items():   
            if license == m365_standard_bundles:
                
                ##### Filter Dict based on M365 Base License Chosen by user #####
                base_result = m365_base_services[m365_base_service]
                base_dict = { key:value for (key,value) in base_result.items() if value != "No"}
                
                ##### Add the EMS Dict based on M365 Base License Chosen by user #####
                ems_result = m365_ems_services[m365_base_service]
                ems_dict = { key:value for (key,value) in ems_result.items() if value != "No" if key != "EMS"}
                
                ##### Add the MDO Dict based on M365 Base License Chosen by user #####
                mdo_result = m365_mdo_services[m365_base_service]
                mdo_dict = { key:value for (key,value) in mdo_result.items() if value != "No" if key != "Defender for Office"}
                
                ##### Add the VoIP Dict based on M365 Base License Chosen by user #####
                voip_result = m365_voip_services[m365_base_service]
                voip_dict = { key:value for (key,value) in voip_result.items() if value != "No" if key != "VoIP"}
                
                ##### Add the W10 Dict based on M365 Base License Chosen by user #####
                w10_result = m365_w10_services[m365_base_service]
                w10_dict = { key:value for (key,value) in w10_result.items() if value != "No" if key != "Windows 10"}
                
                ##### Add the Addon Feature Dict based on M365 Base License Chosen by user #####
                addon_result = m365_addon_services[m365_base_service]
                addon_dict = { key:value for (key,value) in addon_result.items() if value != "No" if key != "Add-Ons"}

                # ##### Add the Addon Feature Dict based on M365 Base License Chosen by user #####
                aad_result = m365_aad_services[m365_base_service]
                aad_dict = { key:value for (key,value) in aad_result.items() if value != "No" if key != "Azure AD Features"} 
                
                ##### Convert the Dicts to a Pandas Dataframe and Clean Up Indexes and Columns #####
                base_plan_table_design = pd.DataFrame.from_dict(base_dict, orient="Index", columns=[f'Included in {license}']).reset_index().rename(columns = {'index':'Base Services'})
                base_egg_plant_list = []
                base_egg_plant_count = 0
                while base_egg_plant_count < len(base_plan_table_design):
                    base_egg_plant_list.append("🍆")
                    base_egg_plant_count += 1
                base_plan_table_design['💦'] = base_egg_plant_list
                base_plan_table_design.set_index('💦', inplace=True)
 
                ems_plan_table_design = pd.DataFrame.from_dict(ems_dict, orient="Index", columns=[f'Included in {license}']).reset_index().rename(columns = {'index':'Enterprise Mobility & Security'})
                ems_egg_plant_list = []
                ems_egg_plant_count = 0    
                while ems_egg_plant_count < len(ems_plan_table_design):
                    ems_egg_plant_list.append("🍆")
                    ems_egg_plant_count += 1
                ems_plan_table_design['💦'] = ems_egg_plant_list
                ems_plan_table_design.set_index('💦', inplace=True)

                mdo_plan_table_design = pd.DataFrame.from_dict(mdo_dict, orient="Index", columns=[f'Included in {license}']).reset_index().rename(columns = {'index':'Microsoft Defender Online'})
                mdo_egg_plant_list = []
                mdo_egg_plant_count = 0    
                while mdo_egg_plant_count < len(mdo_plan_table_design):
                    mdo_egg_plant_list.append("🍆")
                    mdo_egg_plant_count += 1
                mdo_plan_table_design['💦'] = mdo_egg_plant_list
                mdo_plan_table_design.set_index('💦', inplace=True)

                voip_plan_table_design = pd.DataFrame.from_dict(voip_dict, orient="Index", columns=[f'Included in {license}']).reset_index().rename(columns = {'index':'VoIP'})
                voip_egg_plant_list = []
                voip_egg_plant_count = 0    
                while voip_egg_plant_count < len(voip_plan_table_design):
                    voip_egg_plant_list.append("🍆")
                    voip_egg_plant_count += 1
                voip_plan_table_design['💦'] = voip_egg_plant_list
                voip_plan_table_design.set_index('💦', inplace=True)

                w10_plan_table_design = pd.DataFrame.from_dict(w10_dict, orient="Index", columns=[f'Included in {license}']).reset_index().rename(columns = {'index':'Windows 10'})
                w10_egg_plant_list = []
                w10_egg_plant_count = 0    
                while w10_egg_plant_count < len(w10_plan_table_design):
                    w10_egg_plant_list.append("🍆")
                    w10_egg_plant_count += 1
                w10_plan_table_design['💦'] = w10_egg_plant_list
                w10_plan_table_design.set_index('💦', inplace=True)

                addon_plan_table_design = pd.DataFrame.from_dict(addon_dict, orient="Index", columns=[f'Included in {license}']).reset_index().rename(columns = {'index':'Misc. Addons'})
                addon_egg_plant_list = []
                addon_egg_plant_count = 0    
                while addon_egg_plant_count < len(addon_plan_table_design):
                    addon_egg_plant_list.append("🍆")
                    addon_egg_plant_count += 1
                addon_plan_table_design['💦'] = addon_egg_plant_list
                addon_plan_table_design.set_index('💦', inplace=True)

                aad_plan_table_design = pd.DataFrame.from_dict(aad_dict, orient="Index", columns=[f'Included in {license}']).reset_index().rename(columns = {'index':'Azure AD Features'})
                aad_egg_plant_list = []
                aad_egg_plant_count = 0    
                while aad_egg_plant_count < len(aad_plan_table_design):
                    aad_egg_plant_list.append("🍆")
                    aad_egg_plant_count += 1
                aad_plan_table_design['💦'] = aad_egg_plant_list
                aad_plan_table_design.set_index('💦', inplace=True)

                ##### Add Pandas Styles to the Dataframe #####
                base_plan_table_style =  base_plan_table_design.style.set_table_styles([
                            {
                                "selector":"thead",
                                "props": [("background-color", "LightCoral"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            },
                            {
                                "selector":"th.row_heading",
                                "props": [("background-color", "SteelBlue"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-style", "italic")]
                            },
                            {
                                "selector":"th.col_heading",
                                "props": [("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            }
                        ])
                ems_plan_table_style =  ems_plan_table_design.style.set_table_styles([
                            {
                                "selector":"thead",
                                "props": [("background-color", "LightCoral"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            },
                            {
                                "selector":"th.row_heading",
                                "props": [("background-color", "SteelBlue"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-style", "italic")]
                            },
                            {
                                "selector":"th.col_heading",
                                "props": [("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            }
                        ])
                mdo_plan_table_style =  mdo_plan_table_design.style.set_table_styles([
                            {
                                "selector":"thead",
                                "props": [("background-color", "LightCoral"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            },
                            {
                                "selector":"th.row_heading",
                                "props": [("background-color", "SteelBlue"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-style", "italic")]
                            },
                            {
                                "selector":"th.col_heading",
                                "props": [("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            }
                        ])
                voip_plan_table_style =  voip_plan_table_design.style.set_table_styles([
                            {
                                "selector":"thead",
                                "props": [("background-color", "LightCoral"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            },
                            {
                                "selector":"th.row_heading",
                                "props": [("background-color", "SteelBlue"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-style", "italic")]
                            },
                            {
                                "selector":"th.col_heading",
                                "props": [("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            }
                        ])
                w10_plan_table_style =  w10_plan_table_design.style.set_table_styles([
                            {
                                "selector":"thead",
                                "props": [("background-color", "LightCoral"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            },
                            {
                                "selector":"th.row_heading",
                                "props": [("background-color", "SteelBlue"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-style", "italic")]
                            },
                            {
                                "selector":"th.col_heading",
                                "props": [("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            }
                        ])
                addon_plan_table_style =  addon_plan_table_design.style.set_table_styles([
                            {
                                "selector":"thead",
                                "props": [("background-color", "LightCoral"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            },
                            {
                                "selector":"th.row_heading",
                                "props": [("background-color", "SteelBlue"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-style", "italic")]
                            },
                            {
                                "selector":"th.col_heading",
                                "props": [("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            }
                        ])
                aad_plan_table_style =  aad_plan_table_design.style.set_table_styles([
                            {
                                "selector":"thead",
                                "props": [("background-color", "LightCoral"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            },
                            {
                                "selector":"th.row_heading",
                                "props": [("background-color", "SteelBlue"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-style", "italic")]
                            },
                            {
                                "selector":"th.col_heading",
                                "props": [("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            }
                        ])        
                ##### Convert the Dataframe to a Streamlit Table #####        
                col1.table(base_plan_table_style)
                col1.table(ems_plan_table_style)
                col1.table(mdo_plan_table_style)
                col1.table(voip_plan_table_style)
                col1.table(w10_plan_table_style)
                col1.table(addon_plan_table_style)
                col1.table(aad_plan_table_style)

##### Function for the EMS License Dropdown #####                
def featuresProvidedBasedOnChosenEmsBundle():
    for m365_ems_service in m365_ems_services:    
        for feature, license in m365_ems_services[m365_ems_service].items():
            if license == m365_ems_bundles:
                ems_result = m365_ems_services[m365_ems_service]
                ems_dict = { key:value for (key,value) in ems_result.items() if value != "No" if key != "EMS"}
                ems_plan_table_design = pd.DataFrame.from_dict(ems_dict, orient="Index", columns=[license]).reset_index().rename(columns = {'index':'Enterprise Mobility & Security Features'})
                ems_egg_plant_list = []
                ems_egg_plant_count = 0    
                while ems_egg_plant_count < len(ems_plan_table_design):
                    ems_egg_plant_list.append("🍆")
                    ems_egg_plant_count += 1
                ems_plan_table_design['💦'] = ems_egg_plant_list
                ems_plan_table_design.set_index('💦', inplace=True)
                ems_plan_table_style =  ems_plan_table_design.style.set_table_styles([
                            {
                                "selector":"thead",
                                "props": [("background-color", "LightCoral"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            },
                            {
                                "selector":"th.row_heading",
                                "props": [("background-color", "SteelBlue"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-style", "italic")]
                            },
                            {
                                "selector":"th.col_heading",
                                "props": [("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            }
                        ])
                col2.table(ems_plan_table_style)  

##### Function for the MDO License Dropdown #####                
def featuresProvidedBasedOnChosenMdoBundle():
    for m365_mdo_service in m365_mdo_services:    
        for feature, license in m365_mdo_services[m365_mdo_service].items():
            if license == m365_mdo_bundles:
                mdo_result = m365_mdo_services[m365_mdo_service]
                mdo_dict = { key:value for (key,value) in mdo_result.items() if value != "No" if key != "Defender for Office"}
                mdo_plan_table_design =pd.DataFrame.from_dict(mdo_dict, orient="Index", columns=[license]).reset_index().rename(columns = {'index':'Microsoft Defender Online Features'})
                mdo_egg_plant_list = []
                mdo_egg_plant_count = 0    
                while mdo_egg_plant_count < len(mdo_plan_table_design):
                    mdo_egg_plant_list.append("🍆")
                    mdo_egg_plant_count += 1
                mdo_plan_table_design['💦'] = mdo_egg_plant_list
                mdo_plan_table_design.set_index('💦', inplace=True)

                mdo_plan_table_style =  mdo_plan_table_design.style.set_table_styles([
                            {
                                "selector":"thead",
                                "props": [("background-color", "LightCoral"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            },
                            {
                                "selector":"th.row_heading",
                                "props": [("background-color", "SteelBlue"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-style", "italic")]
                            },
                            {
                                "selector":"th.col_heading",
                                "props": [("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            }
                        ])
                col2.table(mdo_plan_table_style)   

##### Function for the W10 License Dropdown #####                
def featuresProvidedBasedOnChosenW10Bundle():
    for m365_w10_service in m365_w10_services:    
        for feature, license in m365_w10_services[m365_w10_service].items():
            if license == m365_w10_bundles:
                w10_result = m365_w10_services[m365_w10_service]
                w10_dict = { key:value for (key,value) in w10_result.items() if value != "No" if key != "Windows 10"}
                w10_plan_table_design = pd.DataFrame.from_dict(w10_dict, orient="Index", columns=[license]).reset_index().rename(columns = {'index':'Windows 10 Features'})
                w10_egg_plant_list = []
                w10_egg_plant_count = 0    
                while w10_egg_plant_count < len(w10_plan_table_design):
                    w10_egg_plant_list.append("🍆")
                    w10_egg_plant_count += 1
                w10_plan_table_design['💦'] = w10_egg_plant_list
                w10_plan_table_design.set_index('💦', inplace=True)
                w10_plan_table_style =  w10_plan_table_design.style.set_table_styles([
                            {
                                "selector":"thead",
                                "props": [("background-color", "LightCoral"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            },
                            {
                                "selector":"th.row_heading",
                                "props": [("background-color", "SteelBlue"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-style", "italic")]
                            },
                            {
                                "selector":"th.col_heading",
                                "props": [("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            }
                        ])
                col2.table(w10_plan_table_style) 
                

##### Function for the AAD License Dropdown #####                
def featuresProvidedBasedOnChosenAadBundle():
    for m365_aad_service in m365_aad_services:    
        for feature, license in m365_aad_services[m365_aad_service].items():
            if license == m365_aad_bundles:
                aad_result = m365_aad_services[m365_aad_service]
                aad_dict = { key:value for (key,value) in aad_result.items() if value != "No" if key != "Azure AD Features"}
                aad_plan_table_design = pd.DataFrame.from_dict(aad_dict, orient="Index", columns=[license]).reset_index().rename(columns = {'index':'Azure AD Features'})
                aad_egg_plant_list = []
                aad_egg_plant_count = 0    
                while aad_egg_plant_count < len(aad_plan_table_design):
                    aad_egg_plant_list.append("🍆")
                    aad_egg_plant_count += 1
                aad_plan_table_design['💦'] = aad_egg_plant_list
                aad_plan_table_design.set_index('💦', inplace=True)
                aad_plan_table_style =  aad_plan_table_design.style.set_table_styles([
                            {
                                "selector":"thead",
                                "props": [("background-color", "LightCoral"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            },
                            {
                                "selector":"th.row_heading",
                                "props": [("background-color", "SteelBlue"), ("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-style", "italic")]
                            },
                            {
                                "selector":"th.col_heading",
                                "props": [("color", "white"),
                                          ("border", "3px solid white"),
                                          ("font-size", "1rem"), ("font-weight:", "bold")]
                            }
                        ])
                col2.table(aad_plan_table_style) 

##### Function for Calculating the Per User License Cost #####
def costPerUserCalculator():
    global total_cost_per_user    
    for key, value in m365_pricing_import.items():
        if key == m365_standard_bundles:
            total_cost_per_user += value
    if m365_ems_bundles != []:
            for key, value in m365_pricing_import.items():
                if key == m365_ems_bundles:
                    total_cost_per_user += value
    if m365_mdo_bundles != []:
            for key, value in m365_pricing_import.items():
                if key == m365_mdo_bundles:
                    total_cost_per_user += value
    if m365_w10_bundles != []:
            for key, value in m365_pricing_import.items():
                if key == m365_w10_bundles:
                    total_cost_per_user += value
    if m365_aad_bundles != []:
        for key, value in m365_pricing_import.items():
            if key == m365_aad_bundles:
                total_cost_per_user += value
##### Estimate Cost for user and Total Cost #####                    
    st.sidebar.metric(label="Cost Per User!", value=float(total_cost_per_user))
    total_user_count_input = st.sidebar.number_input ('How many users do you have?', min_value=0)
    total_user_count_sum = (total_cost_per_user * total_user_count_input)
    total_user_count_sum_round = "{:.2f}".format(total_user_count_sum)
    st.sidebar.metric(label="Estimated Total", value=float(total_user_count_sum_round))


##### Call our Functions! #####
defineVariables()
featuresProvidedBasedOnChosenBaseBundle()
featuresProvidedBasedOnChosenEmsBundle() 
featuresProvidedBasedOnChosenMdoBundle()
featuresProvidedBasedOnChosenW10Bundle()
featuresProvidedBasedOnChosenAadBundle()
costPerUserCalculator()
# security_eggplant_sizing_scale()

