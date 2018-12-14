require "application_system_test_case"

class AmenitiesTest < ApplicationSystemTestCase
  setup do
    @amenity = amenities(:one)
  end

  test "visiting the index" do
    visit amenities_url
    assert_selector "h1", text: "Amenities"
  end

  test "creating a Amenity" do
    visit amenities_url
    click_on "New Amenity"

<<<<<<< HEAD
    fill_in "Hall name", with: @amenity.hall_name
    fill_in "Name", with: @amenity.name
=======
    fill_in "Hall", with: @amenity.hall_id
    fill_in "Name", with: @amenity.name
    fill_in "Status", with: @amenity.status
    fill_in "User", with: @amenity.user_id
>>>>>>> 4ebe9d6d9003f9ee90dc5b2f170c79dac4c134e4
    click_on "Create Amenity"

    assert_text "Amenity was successfully created"
    click_on "Back"
  end

  test "updating a Amenity" do
    visit amenities_url
    click_on "Edit", match: :first

<<<<<<< HEAD
    fill_in "Hall name", with: @amenity.hall_name
    fill_in "Name", with: @amenity.name
=======
    fill_in "Hall", with: @amenity.hall_id
    fill_in "Name", with: @amenity.name
    fill_in "Status", with: @amenity.status
    fill_in "User", with: @amenity.user_id
>>>>>>> 4ebe9d6d9003f9ee90dc5b2f170c79dac4c134e4
    click_on "Update Amenity"

    assert_text "Amenity was successfully updated"
    click_on "Back"
  end

  test "destroying a Amenity" do
    visit amenities_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Amenity was successfully destroyed"
  end
end
