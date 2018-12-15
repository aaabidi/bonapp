Rails.application.routes.draw do
  root 'halls#index'
  resources :amenities do
    resources :statuses
  end
  resources :foods do
    resources :reviews
  end
  resources :halls do
    resources :foods
  end
  devise_for :users, :controllers => {registrations: 'registrations'}
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
