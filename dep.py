import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/arkou/Desktop/deployment/model.pkl', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    

    if (prediction[0] == 0):
      return 'pas fraude'
    else:
      return 'fraude'
  
    
  
def main():
    
    
    # giving a title
    st.title('Fraud Detection App')
    
    
    # getting the input data from the user
    
    
    trafic_otarie_prepaid = st.text_input('trafic_otarie prepaid')
    trafic_IN_prepaid = st.text_input('trafic_IN prepaid')
    trafci_prs_all = st.text_input('trafci_prs_all')
    trafic_otarie_all = st.text_input('trafic_otarie_all')
    trafic_etoile6 = st.text_input('trafic_etoile6')
    trafic_etoile3 = st.text_input('trafic_etoile3')
    trafic_vpn = st.text_input('trafic_vpn')
    
    
    
    # code for Prediction
    pred = ''
    
    # creating a button for Prediction
    
    if st.button('resultat'):
        pred = diabetes_prediction([float(trafic_otarie_prepaid), float(trafic_IN_prepaid), float(trafci_prs_all), float(trafic_otarie_all), float(trafic_etoile6), float(trafic_etoile3), float(trafic_vpn)])
        
        
    st.success(pred)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
