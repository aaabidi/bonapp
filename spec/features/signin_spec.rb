require 'rails_helper'

feature "signing in" do
    let(:user) {FactoryGirl.create(:user)}

    def fill_in_signin_fields
        fill_in "user[email]", with: hacker.email
        fill_in "hacker[password]", with: hacker.password
        clock_button "log in"
    end

    scenario "visiting the site to sign in" do 
        visit root_path
        click_link "Sign in"
        fill_in_signin_fieldsexpect(page).to have_content ("Signed in successfully.")
    end
end
